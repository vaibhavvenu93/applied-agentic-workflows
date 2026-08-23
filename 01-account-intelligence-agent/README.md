# Account Intelligence Agent

Turn a company name into an evidence-backed account intelligence brief.

This is Build #01 in **Applied Agentic Workflows**.

## The Problem

Preparing properly for a company, prospect, partner, founder, or executive usually means jumping across company websites, LinkedIn, news, job postings, interviews, product pages, and search results.

The problem is not access to information.

The problem is turning scattered information into a useful point of view.

## Goal

Build an AI-native research workflow that takes:

- company name
- company website
- target person or role
- optional business problem

and produces:

- company overview
- business model
- products and customers
- recent strategic signals
- hiring and leadership signals
- relevant executive context
- sourced facts
- inferred hypotheses
- likely business problems
- AI and automation opportunities
- "why now?" analysis
- discovery questions
- suggested proof of concept
- outreach angle
- confidence and source evidence

## Core Principle

Facts and hypotheses must never be treated as the same thing.

Every factual claim should be linked to evidence.

Every inference should clearly state that it is an inference.

## Planned Versions

### V0 — Manual Intelligence Schema
Define what good account intelligence actually looks like.

### V1 — CLI Research Tool
Run research from the terminal and generate structured output.

### V2 — Multi-Source Research
Research websites, news, hiring, executives, and other public signals.

### V3 — Opportunity Intelligence
Turn research into business and AI opportunity hypotheses.

### V4 — Evaluation
Score evidence quality, completeness, hallucination risk, and usefulness.

### V5 — Agentic Workflow
Add planning, tool use, retries, and human approval.

### V6 — Interactive App
A simple interface for non-technical users.

## Architecture

```text
Input
  ↓
Research Planner
  ↓
Search + Source Collection
  ↓
Evidence Store
  ↓
Fact Extraction
  ↓
Signal Detection
  ↓
Opportunity Analysis
  ↓
POC Recommendation
  ↓
Evaluation
  ↓
Account Intelligence Brief
