'use client';

import React, { createContext, useContext, useState, useEffect } from "react";
import { usePathname, useRouter } from "next/navigation";
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

const PUBLIC_ROUTES = ["/login", "/register"];

export function AuthProvider({ children }: { children: React.ReactNode }) {
  const [user, setUser] = useState<User | null>(null);
  const [organization, setOrganization] = useState<Organization | null>(null);
  const [token, setToken] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const pathname = usePathname();
  const router = useRouter();

  useEffect(() => {
    try {
      const storedToken = localStorage.getItem("atlas_token");
      const storedUser = localStorage.getItem("atlas_user");
      const storedOrg = localStorage.getItem("atlas_org");

      if (storedToken && storedUser) {
        setToken(storedToken);
        setUser(JSON.parse(storedUser));
        if (storedOrg) setOrganization(JSON.parse(storedOrg));
      } else {
        setUser(null);
        setOrganization(null);
        setToken(null);
        // If not on a public route, redirect to login
        if (!PUBLIC_ROUTES.includes(pathname)) {
          router.push("/login");
        }
      }
    } catch (e) {
      console.error("Failed to load auth state from storage", e);
    } finally {
      setIsLoading(false);
    }
  }, [pathname, router]);

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
    router.push("/login");
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        organization,
        token,
        isAuthenticated: !!user && !!token,
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
