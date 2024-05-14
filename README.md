
<a name="readme-top"></a>

<!-- PROJECT DETAILS -->
<br />
<div align="center">
  <a href="https://github.com/BacHaSoftware/slack_connector">
    <img src="/bhs_odoo_slack/static/description/icon.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Slack Connector</h3>

  <p align="center">
    A product of Bac Ha Software allows users to receive notifications from odoo via Slack account.
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact-us">Contact us</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<div align="left">
  <a href="https://github.com/BacHaSoftware/slack_connector">
    <img src="/bhs_odoo_slack/static/description/imgs/screen/settings.png" alt="Setting">
  </a>
<div align="center">General Settings</div> 
</div>

<div align="left">
  <a href="https://github.com/BacHaSoftware/slack_connector">
    <img src="/bhs_odoo_slack/static/description/imgs/screen/slack.png" alt="Setting">
  </a>
<div align="center">Receive Notification Via Slack</div> 
</div>

#### Key Features:

🌟 <code>General Settings</code>: You'll need to register your Slack app before getting started. The registered app is assigned a unique Client ID and Client Secret to use for OAuth flow. Input them so odoo can connect to Slack.

🌟 <code>Config Workspace</code>: You can connect to multiple workspaces. Configure them in menu Slack connector.

🌟 <code>User Settings</code>: To receive notifications from Odoo via Slack, you need to input Slack User Config and select Handle by Slack in field Notification.

🌟 <code>Receive Notification Via Slack</code>: After configuration is complete, you can receive Odoo notifications via Slack.
<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

<!-- PREREQUISTES  -->
### Prerequisites

This module needs the Python library <code>slackclient</code>, <code>html-slacker</code>, otherwise it cannot be installed and used. Install them through the command
  ```sh
  sudo pip3 install slackclient
  sudo pip3 install html-slacker
  ```

### Installation

1. Install module  <code>bhs_odoo_slack</code>
2. Create App slack and get Client ID, Client Secret and User OAuth Token
3. Config Slack connector and User Settings in Setting Odoo

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage

A product of Bac Ha Software allows unassigned user from task when click avatar user easily.

#### Featured Highlight:

🌟 <code>Simple Setup</code>: Easy to set up connection to workspace. Users can choose to receive notifications via slack or not.

🌟 <code>Slack Integration</code>: Send to Slack messages generated in odoo. Messages can be sent to channel or sent to each member.



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT US-->
## Contact us
Need assistance with setup or have any concerns? Contact Bac Ha Software directly for prompt and dedicated support:
<div align="left">
  <a href="https://github.com/BacHaSoftware">
    <img src="/bhs_odoo_slack/static/description/imgs/logo.png" alt="Logo" height="80">
  </a>
</div>

📨 odoo@bachasoftware.com

🌍 [https://bachasoftware.com](https://bachasoftware.com)

[![WEBSITE][website-shield]][website-url] [![LinkedIn][linkedin-shield]][linkedin-url]

Project Link: [https://github.com/BacHaSoftware/slack_connetor](https://github.com/BacHaSoftware/slack_connetor)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[license-url]: https://github.com/BacHaSoftware/slack_connetor/blob/17.0/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/company/bac-ha-software
[website-shield]: https://img.shields.io/badge/-website-black.svg?style=for-the-badge&logo=website&colorB=555
[website-url]: https://bachasoftware.com