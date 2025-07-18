#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]
class Person:
    approved_jobs = ["Sales", "Engineering", "HR", "Marketing", "ITC"]

    def __init__(self, name=None, job=None):
        if name is not None:
            if not isinstance(name, str) or not (1 <= len(name) <= 25):
                print("Name must be string between 1 and 25 characters.")
            else:
                self.name = name.title()

        if job is not None:
            if not isinstance(job, str) or job not in Person.approved_jobs:
                print("Job must be in list of approved jobs.")
            else:
                self.job = job
