# code1
Course code
# Requisition App

A Python application that manages staff item requisitions, calculates total costs, and determines approval based on budget thresholds.

## Features

- Collects staff and item details via user input
- Calculates total cost for a set of items
- Determines approval status
- Generates a unique approval reference
- Displays all requisition details

## Software Design Principles Applied

### 1. **Encapsulation**
Each `Requisition` instance contains its own state, such as `staff_data`, `items`, and `total_cost".

### 2. **Abstraction**
The complexity of how a requisition works (e.g. ID generation, cost calculation) is hidden within a function. The user only interacts with the class through well-defined inputs.

### 3. **Separation of Concerns**
- `staff_info()` handles staff input
- `requisition_totals()` deals with item input
- `requisition_approval()` decides approval
- `display_requisitions()` handles output
