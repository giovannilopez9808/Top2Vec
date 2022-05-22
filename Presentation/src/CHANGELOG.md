# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

### Fixed

- Typo in demo

## [0.6.6] - 2022-05-08

### Fixed

- Issue when \biglogo or \smalllogo were used without argument

## [0.6.5] - 2022-05-08

### Fixed

- Clip triangles to slide frame to overflow issues with handout with notes

## [0.6.4] - 2022-03-19

### Fixed

- Issue with relative paths (#5)

## [0.6.3] - 2022-03-10

### Changed

- Add options to `\biglogo` and `\smalllogo` that can be passed to
  `\includegraphics` (fixes #5)

## [0.6.2] - 2021-11-10

### Changed

- Improve code style (indent, etc)
- Make sure macrocode is properly indented in docs
- Minor makefile changes
- Remove screenshots from repo to save space, generate them using CI/CD instead

## [0.6.1] - 2021-10-28

### Fixed

- Improve block environment aligment (see #4)

### Changed

- Increase line spacing a tiny bit
- Adjust docs and links related to Overleaf

## [0.6.0] - 2021-09-06

### Added

- Dark theme support

## [0.5.1] - 2021-03-29

### Fixed

- Fix mishandling of backgrounds with trigonset

### Changed

- Install documentation now mention CTAN url

## [0.5.0] - 2021-03-25

### Added

- New cyber background for regular slides
- Add alternative demo

### Changed

- Update screenshots for readme

## [0.4.0] - 2021-03-25

### Added

- Individual test for each option
- Add trigon set option
- Add font patch from metropolis

### Changed

- Improve screenshots to illustrate layout options
- Handle no logos/titlegraphic situations
- Minor changes in the theme demo

## [0.3.0] - 2021-02-27

### Added

- Makefile
- Proper documentation
- Changelog

### Changed

- Adopt Documented Latex Format (dtx)
- Change option `nosourcefont` to `usesourcefont`

### Remove

- Remove alternative demo texfile
- Remove old .sty files
- Remove redundant options

## [0.2] - 2021-01-30

### Added

- Options for title fonts

### Changed

- Default block style from transparent to fill
- Define same origin for titlegraphic box for the titlepage layouts
- Simplify color theme definition
- Lower images resolution
- Possibility to disable sourcesansfont

### Removed

- Unnecessary package tcolorbox

## 0.1 - 2021-01-27

- Initial commit

[Unreleased]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.6.6...master
[0.6.6]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.6.5...v0.6.6
[0.6.5]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.6.4...v0.6.5
[0.6.4]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.6.3...v0.6.4
[0.6.3]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.6.2...v0.6.3
[0.6.2]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.6.1...v0.6.2
[0.6.1]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.6.0...v0.6.1
[0.6.0]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.5.0...v0.6.0
[0.5.0]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.4.0...v0.5.0
[0.4.0]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.3.0...v0.4.0
[0.3.0]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.2...v0.3.0
[0.2]: https://gitlab.com/thlamb/beamertheme-trigon/-/compare/v0.1...v0.2
