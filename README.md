# security-behavior-clustering
Unsupervised behavior clustering for security analytics using Python and NumPy
# Security Behavior Clustering (Unsupervised)

This project implements **unsupervised behavior clustering** from first principles using **Python and NumPy only**. The goal is to demonstrate how clustering logic works under the hood and how it can be applied to **security analytics, SOC workflows, and cloud security use cases**.

Rather than relying on high-level machine learning libraries, this implementation focuses on **core algorithmic understanding**, correctness, and reproducibility.

---

##  What This Project Demonstrates

From a security and cloud perspective, this project maps directly to:

* Behavioral baselining for users, hosts, or cloud workloads
* Unsupervised anomaly detection
* Security log and event clustering
* Noise reduction and signal grouping in SOC environments
* Foundations for ML-driven detection engineering

Under the hood, the clustering logic is equivalent to **centroid-based clustering (k-means)**, but the emphasis is on **behavior modeling**, which is how this technique is commonly described in security operations.

---

##  Core Concepts Implemented

* Squared Euclidean distance calculation
* Deterministic point-to-centroid assignment
* Iterative centroid updates
* Convergence behavior
* Explicit handling of empty clusters
* Clean, modular, import-safe design

-----------------------------------------------------------------------------------------------------

## 📁 Repository Structure

```text
security-behavior-clustering/
│
├── behavior_clustering.py   # Clean, professional version (public-facing)
├── pweek8.py                # Original academic submission version
├── README.md
└── data/                    # Example centroid datasets (optional)
--------------------------------------------------------------------------------------------

## ⚙️ Functions Overview

### `Centroid(L)`

Computes the centroid (mean point) of a set of 2D points.

### `CreateCentroids(K)`

Initializes `K` centroids using a fixed random seed for reproducibility.

### `CentroidAssignment(L, C)`

Assigns each data point to the closest centroid using squared distance.

### `NewCentroids(L, A, K)`

Recomputes centroids based on current assignments and handles empty clusters safely.

---

##  How to Use (Local Testing)

```python
import numpy as np
from behavior_clustering import *

L = np.loadtxt("centroid-data-example.txt", delimiter=",").T
K = 3
C = CreateCentroids(K)

for _ in range(30):
    A = CentroidAssignment(L, C)
    C_new = NewCentroids(L, A, K)
    if np.allclose(C, C_new, equal_nan=True):
        break
    C = C_new
-------------------------------------------------------------------------------------------------

## 🔐 Security & Cloud Use Cases

This foundational implementation applies directly to:

* UEBA (User and Entity Behavior Analytics)
* CloudTrail / Azure AD / GCP audit log analysis
* Detection engineering and threat hunting
* Behavioral anomaly detection
* Security data preprocessing for ML pipelines

In production systems, these ideas appear in tools such as SIEMs, XDR platforms, and cloud-native security services.

---

##  Why This Project Matters

Security teams increasingly rely on **data-driven detection and analytics**. Understanding how clustering works at a fundamental level helps practitioners:

* Tune detections effectively
* Reduce false positives
* Interpret ML-based alerts
* Build trust in automated security systems

This project reflects a transition toward **AI-enabled security analytics** while maintaining a strong grounding in security operations.

---

## 📌 Tech Stack

* Python 3
* NumPy

No external ML libraries were used.

---

## 📬 Feedback & Discussion

Feedback, suggestions, and discussion are always welcome. This project is part of an ongoing focus on **security analytics, cloud security, and applied machine learning**.

If you are a recruiter or security professional, feel free to reach out or explore the code for a deeper technical review.
