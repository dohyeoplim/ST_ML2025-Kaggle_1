### **1.**

### **High Variability in Convective Activity**





-   Summer has **localized convective events** (e.g., afternoon thunderstorms) driven by heat, moisture, and instability.
-   These events create **large sub-daily temperature swings** that are **poorly captured by daily aggregates**.
-   Prediction suffers if the model can’t anticipate sudden cloud formation, rainfall, or convective cooling.







### **2.** 

### **Cloud Cover Uncertainty**





-   Cloudiness in summer changes rapidly and **strongly affects radiation budget**:

    

    -   ☀️ Clear skies → high temp
    -   ☁️ Afternoon cumulus → suppressed peak temp

    

-   Models often underperform if they don’t model cloud formation dynamics indirectly (e.g., via moisture convergence or vertical instability proxies).







### **3.** 

### **Humidity and Dew Point**





-   Summer humidity is high but **variable**. This affects:

    

    -   Radiation (greenhouse trapping)
    -   Dew point spread (temp-dew gap shrinks)
    -   Nighttime cooling (often suppressed)

    

-   If dew point features aren’t properly crafted, model underestimates heat retention.







### **4.** 

### **Sea Breeze and Coastal Modulation**





-   Sea breeze in coastal Korea leads to **strong localized anomalies** in max temp.
-   Daily model may not capture *onshore vs offshore flow* from basic wind stats.







### **5.** 

### **Less Dominant Synoptic Control**





-   Winter: anomalies driven by large, slow systems (e.g., Siberian High)
-   Summer: **chaotic, mesoscale drivers**, not easily captured in surface pressure alone





------





## **✅ Summer-Specific Feature Engineering Improvements**



| **Strategy**                       | **Description**                                              |
| ---------------------------------- | ------------------------------------------------------------ |
| **Convective potential proxy**     | Use temp_max - dew_point_min to approximate instability      |
| **Moisture convergence proxy**     | High humidity_mean, wind_v_mean (southerly) → moisture influx |
| **Midday delta**                   | surface_temp_15 - surface_temp_9 to measure heating slope    |
| **Sunblock potential**             | Use cloud_cover_std + cloud_cover_max to infer afternoon cloudiness |
| **Suppressed cooling flag**        | If dew_temp_gap_mean < 3 and wind_speed_mean < 1, then likely hot/humid night |
| **Sea breeze flag (coastal only)** | Create flag if wind_dir_mean ≈ east/southeast and latitude < X |