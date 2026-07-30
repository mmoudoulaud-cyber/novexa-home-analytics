# Data Dictionary

**Project:** Novexa Home Analytics

**Version:** 1.0

**Status:** Draft

**Author:** Merryl Moudoulaud

**Date:** July 2026

---

## Purpose

This document describes the business entities, tables and fields used in the Novexa Home Analytics data model.

It serves as the reference document for Python ETL, SQL development and Power BI reporting.

---

# Table: Dim_Date

| Column | Data Type | Description | Example |
|---------|-----------|-------------|---------|
| Date_ID | Integer | Unique identifier for each calendar date | 20260115 |
| Date | Date | Calendar date | 2026-01-15 |
| Day | Integer | Day of month | 15 |
| Month | Integer | Month number | 1 |
| Month_Name | Text | Month name | January |
| Quarter | Integer | Quarter number | 1 |
| Year | Integer | Calendar year | 2026 |
| Week | Integer | ISO week number | 3 |
| Day_Name | Text | Day of week | Thursday |
| Is_Weekend | Boolean | Indicates weekend or weekday | False |

