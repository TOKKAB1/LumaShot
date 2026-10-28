# Changelog

This file describes the source version included in this repository. It does not imply that a GitHub Release has been published.

## 5.0.1

- Separate cursor preferences for screenshots and video recordings.
- Keep the existing screenshot choice; show the cursor in new recordings by default.
- Persist both switches independently in the local JSON.
- Apply the matching cursor setting to recording selection previews and video frames.
- Add translated checkboxes and tooltips in RO/RU/EN, with screenshots refreshed in both themes.
- Include the standalone BAT builder; ignore local build files in Git.

## v5 (5.0.0)

- Fixed the OCR window opening behind the always-on-top capture overlay on Windows; it now opens above the capture and receives keyboard focus.
- Extract text from a selected screenshot using the bottom toolbar's OCR button.
- Review, edit, select and copy recognized text without closing the capture.
- Local Windows OCR with installed language selection and no new Python dependencies.
- An Updates tab with manual checking and optional startup checks, disabled by default.
- Download and verify GitHub installer assets; start an interactive installer only on request.
- Finish captures and unsaved video reviews before an update can start.
- Recognize the legacy v4 release as 0.4.0 from its installer filename.
- Onefile EXE version metadata is generated from APP_VERSION in the application.
