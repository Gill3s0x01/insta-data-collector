# Instagram Profile Data Fetcher

This Python script uses the `instaloader` library to retrieve public profile information from Instagram.

## Description

The script takes an Instagram username as input and returns various profile details such as user ID, full name, biography, follower count, and more. Note that sensitive information like email and phone number is **not available** through the public API and thus is indicated as unavailable.

## Features

- Fetches basic public profile information:
  - User ID
  - Username
  - Full Name
  - Biography
  - External URL
  - Verification status
  - Privacy status
  - Number of followers
  - Number of followees
  - Number of posts
  - Profile picture URL
- Handles errors gracefully if the username is invalid or network issues occur.

## Requirements

- Python 3.x
- `instaloader` library

Install `instaloader` via pip:

```bash
pip install instaloader
```

## Usage

Run the script and enter the Instagram username when prompted:

```bash
python spy.py
```

Example:

```
Enter the Instagram profile username you want to fetch: instagram
User ID: 25025320
Username: instagram
Full Name: Instagram
Bio: Bringing you closer to the people and things you love.
External URL: https://about.instagram.com
Is Verified: True
Is Private: False
Followers: 500000000
Followees: 50
Number of Posts: 7000
Profile Picture URL: https://instagram.com/profile_pic_url.jpg
Email: Not available via public API
Phone: Not available via public API
```

## Notes

- This script uses public Instagram data accessible without login.
- Email and phone data are not provided by Instagram's public API for privacy reasons.
- For private or restricted profiles, data might not be accessible.
