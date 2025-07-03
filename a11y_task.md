
**Task Title:**
Develop a Browser-Based Accessibility Testing Agent for Reflow and Resize Text (WCAG 2.2 SC 1.4.4)

**Background:**
Web accessibility ensures that websites are usable by people with disabilities. According to [WCAG 2.2 Success Criterion 1.4.4: Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html), users must be able to resize text up to 200% without loss of content or functionality and without requiring horizontal scrolling. This is crucial for users with low vision who rely on increased text size for readability.

**Task Overview:**
You are required to develop an **automated agent** that operates in a browser environment to test whether a website meets the requirements of WCAG 2.2 SC 1.4.4. The agent should:

- Use **Playwright** for browser automation and structured accessibility data extraction.
- Integrate a **vision-language model (vision-LM)** to analyze visual layout and detect reflow issues caused by resizing text.
- Identify and report any accessibility issues that occur when text is resized up to 200%, specifically focusing on:
    - Loss of content or functionality
    - Introduction of horizontal scrolling
    - Overlapping or cut-off elements

**Detailed Requirements:**

1. **Environment Setup**
    - Use Playwright for web browser operations.
    - Integrate a vision-language model (such as a pre-trained vision-LM) capable of analyzing rendered browser pages for layout issues after text resizing.
2. **Testing Workflow**
    - Load a target web page in a browser session controlled by your agent.
    - Programmatically increase the base text size by resizing the windowsize to 200% using Playwright.
    - Capture screenshots before and after resizing using Playwright.
    - Use the vision-LM to analyze the post-resize rendering for:
        - Overlapping, truncated, or hidden content
        - Loss of interactive elements or functionality
3. **Reporting**
    - Generate a structured report (JSON or Markdown) that includes:
        - A summary of detected issues, referencing the specific WCAG 2.2 SC 1.4.4 criteria
        - Screenshots before and after resizing
        - Remediation suggestions for each detected issue


**Deliverables:**

- Source code (with clear instructions for setup and running the agent)
- Sample report for at least one public website
- Brief documentation explaining your approach and design choices

**Evaluation Criteria:**

- Correctness and completeness of the agent’s detection of reflow and resize text issues
- Effective use of Playwright and vision-LM
- Code quality, readability, and documentation
- Clarity and usefulness of the generated accessibility report

**References:**

- [WCAG 2.2 SC 1.4.4: Resize Text](https://www.w3.org/WAI/WCAG22/Understanding/resize-text.html)
- [Playwright documentation](https://github.com/microsoft/playwright)