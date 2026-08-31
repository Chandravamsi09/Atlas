import * as React from "react";
import { cn } from "@/lib/utils";

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: "primary" | "secondary" | "outline" | "danger" | "ghost";
  size?: "sm" | "md" | "lg";
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ className, variant = "primary", size = "md", ...props }, ref) => {
    const baseStyles = "inline-flex items-center justify-center font-medium transition-colors rounded-lg focus:outline-none focus:ring-2 focus:ring-indigo-500/50 disabled:opacity-50";
    
    const variants = {
      primary: "bg-indigo-600 hover:bg-indigo-500 text-white shadow-sm",
      secondary: "bg-slate-800 hover:bg-slate-700 text-slate-200",
      outline: "border border-slate-700 hover:bg-slate-800 text-slate-300",
      danger: "bg-rose-600 hover:bg-rose-500 text-white",
      ghost: "hover:bg-slate-800/60 text-slate-400 hover:text-slate-200"
    };

    const sizes = {
      sm: "px-2.5 py-1.5 text-xs",
      md: "px-4 py-2 text-sm",
      lg: "px-6 py-3 text-base"
    };

    return (
      <button
        ref={ref}
        className={cn(baseStyles, variants[variant], sizes[size], className)}
        {...props}
      />
    );
  }
);
Button.displayName = "Button";
