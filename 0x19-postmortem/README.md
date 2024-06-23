# 0x19. Postmortem

`#DevOps` `#SysAdmin`

## Project Overview

**Project Start Date:** June 17, 2024, 4:00 AM UTC
**Project End Date:** June 24, 2024, 4:00 AM UTC

## Background Context

Failures are inevitable in any software system, whether they stem from bugs, traffic spikes, security issues, hardware failures, natural disasters, or human error. However, each failure presents an opportunity to learn and improve. A great Software Engineer must learn from these incidents to prevent recurrence. A postmortem is a widely used tool in the tech industry to analyze outages and ensure preventive measures are implemented.

## Purpose of a Postmortem

A postmortem serves two main purposes:

1. To provide the rest of the company's employees with detailed information about the cause of the outage. This is crucial because outages can significantly impact a company, and managers and executives need to understand what happened and how it will affect their work.
2. To ensure that the root cause(s) of the outage have been identified and that measures are taken to prevent recurrence.

## Tasks

### 0. My First Postmortem (Mandatory)

Using an issue from one of the web stack debugging projects or an outage you have personally faced, write a postmortem. If you haven't faced an outage, get creative and invent your own.

#### Requirements:

1. **Issue Summary:**

- Duration of the outage with start and end times (including timezone)
- Impact (what service was down/slow, what users were experiencing, how many % of users were affected)
- Root cause

2. **Timeline (bullet point format, short 1-2 sentences):**

- When the issue was detected
- How the issue was detected (monitoring alert, an engineer noticed, customer complaint, etc.)
- Actions taken (system parts investigated, assumptions on root cause)
- Misleading investigation/debugging paths taken
- Team/individuals the incident was escalated to
- How the incident was resolved

3. **Root Cause and Resolution:**

- Detailed explanation of what caused the issue
- Detailed explanation of how the issue was fixed

4. **Corrective and Preventative Measures:**
- Broad improvements/fixes
- Specific tasks to address the issue (e.g., patch Nginx server, add monitoring on server memory)

**Note:** Be brief and straight to the point, between 400 to 600 words.

### 1. Make People Want to Read Your Postmortem (Advanced)

To capture attention in an information-overloaded environment, make your postmortem engaging by adding humor, diagrams, or anything visually appealing.

## Example Postmortem

[Google API infrastructure outage incident report](https://intranet.alxswe.com/rltoken/vkEjk-M6yBWW-wyB-7-I9Q)

By following this structured approach to writing postmortems, you can effectively communicate incidents' causes and resolutions, ensuring continuous improvement in your software systems.
