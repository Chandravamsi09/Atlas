'use client';

import React, { createContext, useContext, useState, useEffect } from "react";
import { api, getAuthToken, setAuthSession, clearAuthSession } from "@/lib/api";

interface User {
  id: string;
  email: string;
  full_name: string;
}

interface Organization {
  id: string;
  name: string;
  slug: string;
  role: string;
}

interface AuthContextType {
  user: User | null;
  organization: Organization | null;
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string, fullName: string, orgName?: string) => Promise<void>;
  logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [organization, setOrganization] = useState<Organization | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Check localStorage on initial load
    try {
      const storedToken = localStorage.getItem("atlas_token");
      const storedUser = localStorage.getItem("atlas_user");
      const storedOrg = localStorage.getItem("atlas_org");

      if (storedToken && storedUser) {
        setToken(storedToken);
        setUser(JSON.parse(storedUser));
        if (storedOrg) setOrganization(JSON.parse(storedOrg));
      } else {
        // Seed default developer account for immediate testing
        const defaultUser: User = { id: "usr_admin_01", email: "admin@atlas.ai", full_name: "Atlas Administrator" };
        const defaultOrg: Organization = { id: "org_acme_prod_01", name: "Acme Corporation", slug: "acme-corp", role: "owner" };
        setUser(defaultUser);
        setOrganization(defaultOrg);
      }
    } catch (e) {
      console.error("Failed to load auth state from storage", e);
    } finally {
      setIsLoading(false);
    }
  }, []);

  const login = async (email: string, password: string) => {
    setIsLoading(true);
    try {
      const res = await api.auth.login({ email, password });
      setToken(res.access_token);
      setUser(res.user);
      setOrganization(res.organization);
      setAuthSession(res.access_token, res.user, res.organization);
    } finally {
      setIsLoading(false);
    }
  };

  const register = async (email: string, password: string, fullName: string, orgName?: string) => {
    setIsLoading(true);
    try {
      const res = await api.auth.register({ email, password, full_name: fullName, organization_name: orgName });
      setToken(res.access_token);
      setUser(res.user);
      setOrganization(res.organization);
      setAuthSession(res.access_token, res.user, res.organization);
    } finally {
      setIsLoading(false);
    }
  };

  const logout = () => {
    clearAuthSession();
    setUser(null);
    setOrganization(null);
    setToken(null);
    if (typeof window !== "undefined") {
      window.location.href = "/login";
    }
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        organization,
        token,
        isAuthenticated: !!user,
        isLoading,
        login,
        register,
        logout,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
}
