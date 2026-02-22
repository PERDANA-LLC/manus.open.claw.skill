---
name: oc-healthcheck
description: Performs a security and risk assessment of the host environment. Use when asked for security audits, firewall configuration, SSH hardening, software update checks, or to review the overall security posture of the system.
---

# Host Security Health Check

## When to Use

- When the user asks for a "security audit," "health check," or "security scan."
- When the user wants to harden the system's security settings (e.g., firewall, SSH).
- To check for available software updates and apply them.
- To assess the system's network exposure and listening services.
- Before deploying an application to ensure the host environment is secure.

## Workflow

### 1. Establish Context (Read-Only)

Begin by gathering information about the system to understand its configuration and security posture. Obtain explicit user permission before running any commands.

**Information to Gather:**
1.  **OS and Version:** Use `cat /etc/os-release`.
2.  **Privilege Level:** Check with `whoami` and `groups`.
3.  **Network Exposure:** Identify listening ports with `ss -ltnup`.
4.  **Firewall Status:** Check with `sudo ufw status` or `sudo nft list ruleset`.
5.  **Disk Encryption:** Check for LUKS encryption.
6.  **Automatic Updates:** Check the status of unattended-upgrades.

### 2. Determine Risk Tolerance

After gathering context, ask the user to define their risk tolerance. This will guide the remediation plan. Present the following profiles as numbered options:

1.  **Hardened:** Deny-by-default inbound firewall, minimal open ports, key-only SSH, no root login, automatic security updates enabled. Suitable for production servers.
2.  **Balanced:** A reasonable default for workstations. Firewall enabled, remote access restricted, and regular updates encouraged.
3.  **Developer:** More permissive, allowing local services for development, but with clear warnings about exposure.
4.  **Custom:** Allow the user to specify their own security requirements.

### 3. Produce a Remediation Plan

Based on the gathered context and the user's chosen risk profile, create a step-by-step remediation plan. The plan should include:

- The target security profile.
- A summary of the current security posture.
- The identified gaps between the current state and the target.
- The exact commands to be executed for remediation.
- A rollback plan for each change.
- A clear explanation of the risks involved.

Always present the plan to the user for approval before making any changes.

### 4. Execute with Confirmation

Once the user approves the plan, execute each step. For each command:

- Display the exact command to be run.
- Explain its impact and the rollback procedure.
- Request explicit confirmation from the user before execution.
- Stop immediately if any command produces unexpected output and ask for guidance.

### 5. Verify and Report

After executing the plan, re-run the initial checks to verify that the changes have been applied correctly and that the system is in the desired state.

**Verification Steps:**
- Check firewall status.
- List listening ports to confirm only expected services are exposed.
- Verify that remote access (if configured) is still functional.

Provide a final report to the user summarizing the actions taken and the new security posture of the system.

## Required Confirmations

Always require explicit user approval before:

- Changing firewall rules.
- Opening or closing network ports.
- Modifying SSH configuration.
- Installing, removing, or updating packages.
- Enabling or disabling system services.
- Changing user or group permissions.
- Scheduling any recurring tasks (e.g., via cron).
