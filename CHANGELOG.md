# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 12-10-2024

### Added

- Docstrings throughout

## [0.3.0] - 09-10-2024

### Breaking Changes

- No longer outputs CSV files
- Entire I/O now interacts with MySQL database

### Added

- Ability to set user-defined arbitrary delimiter in shelve generation
- Functionality to edit machine information (only delete for now, but more features coming soon)

## [0.2.0] - 09-10-2024

### Added

- main.py launches program from one location rather than separate modules

### Changed

- All .pngs now get created in the appropriate location
- All submodules get called by main.py
- Sorted all imports
- Formatted entire codebase

## [0.1.0] - 09-10-2024

### Added

- Functionality to generate physical shelf tags
- Functionality to tie machine to location and create csv outfile

### Fixed

- Serial number is now the name of the .png file generated per machine
- The only information directly encoded within the QR Code is the machine serial number; everything else is a lookup

### Changed

- Minor refactoring
- Generated tags now save with self name or serial number, depending on tag
- QR Code outputs now save to generated_codes folder

## [0.0.1] - 03-10-2024

### Created Repository

- CHANGELOG.md
- LICENSE.md
- ccqr.py
- README.md
