import React from "react";
import { AppButton } from "@company/ui";

export type PrimaryButtonProps = {
  children?: React.ReactNode;
  disabled?: boolean;
  loading?: boolean;
};

export function PrimaryButton({
  children = "Submit",
  disabled = false,
  loading = false,
}: PrimaryButtonProps) {
  return (
    <AppButton variant="primary" disabled={disabled} loading={loading}>
      {children}
    </AppButton>
  );
}
