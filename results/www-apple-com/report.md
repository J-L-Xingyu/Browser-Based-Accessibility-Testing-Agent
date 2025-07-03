# Accessibility Report

**URL tested**: https://www.apple.com/  
**Resize Percent**: 200%  
**WCAG SC**: 1.4.4 Resize Text  
**Generated At**: 2025-07-03 00:52:05

---

## ✅ Summary

- **Status**: ❌ Issues found
- **Total issues**: 1
  - ContentLoss: 1
  - HorizontalScroll: 0
  - OverlappingElements: 0

---

## 📸 Screenshots

| Before Resize | After Resize |
| -------------- | ------------- |
| ![Before](before.png) | ![After](after.png) |

---

## 🗂️ Issues Details

### 1️⃣ Type: ContentLoss

**Description:**  
When the text size is increased to 200%, the main navigation bar does not reflow. This causes links at the end of the bar, such as 'Support', the search icon, and the shopping bag icon, to be pushed off-screen and become inaccessible without horizontal scrolling.

**Suggestion:**  
Implement a responsive navigation bar that adapts to content size. For example, collapse the navigation links into a 'hamburger' menu when there is not enough horizontal space.


---


## 🗄️ Raw Model Output

<details>
<summary>Click to expand raw JSON output</summary>


```json
{
  "issues": [
    {
      "type": "ContentLoss",
      "description": "When the text size is increased to 200%, the main navigation bar does not reflow. This causes links at the end of the bar, such as 'Support', the search icon, and the shopping bag icon, to be pushed off-screen and become inaccessible without horizontal scrolling.",
      "suggestion": "Implement a responsive navigation bar that adapts to content size. For example, collapse the navigation links into a 'hamburger' menu when there is not enough horizontal space."
    }
  ]
}
```

</details>
