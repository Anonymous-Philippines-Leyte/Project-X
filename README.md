# Project-X
exploitations defense code.


<p align="center">
 <img width="100px" src="https://avatars.githubusercontent.com/u/139189486?s=400&u=4eb5fd1644b1162126c44c5dff62165a48acdc1c&v=4" align="center" alt="GitHub Christian's Stats" />
 <h2 align="center">GitHub Christian Barbosa's Stats</h2>
 <p align="center">Get dynamically generated GitHub stats on your READMEs!</p>
</p>
  <p align="center">
    <a href="https://github.com/lightdarkmaster/github-readme-stats/actions">
      <img alt="Tests Passing" src="https://github.com/lightdarkmaster/github-readme-stats/workflows/Test/badge.svg" />
    </a>
    <a href="https://github.com/lightdarkmaster/github-readme-stats/graphs/contributors">
      <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/lightdarkmaster/github-readme-stats" />
    </a>
    <a href="https://codecov.io/gh/lightdarkmaster/github-readme-stats">
      <img alt="Tests Coverage" src="https://codecov.io/gh/lightdarkmaster/github-readme-stats/branch/master/graph/badge.svg" />
    </a>
    <a href="https://github.com/lightdarkmaster/github-readme-stats/issues">
      <img alt="Issues" src="https://img.shields.io/github/issues/lightdarkmaster/github-readme-stats?color=0088ff" />
    </a>
    <a href="https://github.com/lightdarkmaster/github-readme-stats/pulls">
      <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/lightdarkmaster/github-readme-stats?color=0088ff" />
    </a>
    <a href="https://securityscorecards.dev/viewer/?uri=github.com/lightdarkmaster/github-readme-stats">
      <img alt="OpenSSF Scorecard" src="https://api.securityscorecards.dev/projects/github.com/lightdarkmaster/github-readme-stats/badge" />
    </a>
    <br />
    <br />
    <a href="https://vercel.com?utm\_source=github\_readme\_stats\_team\&utm\_campaign=oss">
      <img src="./powered-by-vercel.svg"/>
    </a>
  </p>

  <p align="center">
    <a href="#all-demos">View Demo</a>
    ·
    <a href="https://github.com/lightdarkmaster/github-readme-stats/issues/new?assignees=&labels=bug&projects=&template=bug_report.yml">Report Bug</a>
    ·
    <a href="https://github.com/lightdarkmaster/github-readme-stats/issues/new?assignees=&labels=enhancement&projects=&template=feature_request.yml">Request Feature</a>
    ·
    <a href="https://github.com/lightdarkmaster/github-readme-stats/discussions/1770">FAQ</a>
    ·
    <a href="https://github.com/lightdarkmaster/github-readme-stats/discussions/new?category=q-a">Ask Question</a>
  </p>
  <p align="center">
    <a href="/docs/readme_fr.md">Français </a>
    ·
    <a href="/docs/readme_cn.md">简体中文</a>
    ·
    <a href="/docs/readme_es.md">Español</a>
    ·
    <a href="/docs/readme_de.md">Deutsch</a>
    ·
    <a href="/docs/readme_ja.md">日本語</a>
    ·
    <a href="/docs/readme_pt-BR.md">Português Brasileiro</a>
    ·
    <a href="/docs/readme_it.md">Italiano</a>
    ·
    <a href="/docs/readme_kr.md">한국어</a>
    ·
    <a href="/docs/readme_nl.md">Nederlands</a>
    ·
    <a href="/docs/readme_np.md">नेपाली</a>
    ·
    <a href="/docs/readme_tr.md">Türkçe</a>
  </p>
</p>

<a href="https://indiafightscorona.giveindia.org">
  <img src="https://cfstatic.give.do/logo.png" alt="Give india logo" width="200" />
</a>

Are you considering supporting the project by donating to me? Please DO NOT!!!

<img src="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fichef.bbci.co.uk%2Fnews%2F1024%2Fmedia%2Fimages%2F64395000%2Fjpg%2F_64395304_anonymous_demo_afp464x261.jpg&f=1&nofb=1&ipt=e7ec607650e48b2d8189167d194b2d370474770d3a663a727fb83868374d0174&ipo=images" alt="Pictures of Annonymous PH" width="35%">

" We are Legion. We do not forgive. We do not forget. Expect us."

</p>

# Features <!-- omit in toc -->

- [GitHub Stats Card](#github-stats-card)
    - [Hiding individual stats](#hiding-individual-stats)
    - [Showing additional individual stats](#showing-additional-individual-stats)
    - [Showing icons](#showing-icons)
    - [Themes](#themes)
    - [Customization](#customization)
- [GitHub Gist Pins](#github-gist-pins)
    - [Usage](#usage-1)
    - [Demo](#demo-1)
- [Top Languages Card](#top-languages-card)
    - [Usage](#usage-2)
    - [Language stats algorithm](#language-stats-algorithm)
    - [Exclude individual repositories](#exclude-individual-repositories)
    - [Hide individual languages](#hide-individual-languages)
    - [Show more languages](#show-more-languages)
    - [Compact Language Card Layout](#compact-language-card-layout)
    - [Donut Chart Language Card Layout](#donut-chart-language-card-layout)
    - [Donut Vertical Chart Language Card Layout](#donut-vertical-chart-language-card-layout)
    - [Pie Chart Language Card Layout](#pie-chart-language-card-layout)
    - [Hide Progress Bars](#hide-progress-bars)
    - [Demo](#demo-2)
- [All Demos](#all-demos)
  - [Quick Tip (Align The Cards)](#quick-tip-align-the-cards)
- [Deploy on your own](#deploy-on-your-own)
  - [On Vercel](#on-vercel)
    - [:film\_projector: Check Out Step By Step Video Tutorial By @codeSTACKr](#film_projector-check-out-step-by-step-video-tutorial-by-codestackr)
  - [On other platforms](#on-other-platforms)
  - [Disable rate limit protections](#disable-rate-limit-protections)
  - [Keep your fork up to date](#keep-your-fork-up-to-date)
- [:sparkling\_heart: Support the project](#sparkling_heart-support-the-project)

# Important Notices <!-- omit in toc -->

> [!IMPORTANT]\
> Since the GitHub API only [allows 5k requests per hour per user account](https://docs.github.com/en/graphql/overview/resource-limitations), the public Vercel instance hosted on `https://github-readme-stats.vercel.app/api` could possibly hit the rate limiter (see [#1471](https://github.com/lightdarkmaster/github-readme-stats/issues/1471)). We use caching to prevent this from happening (see https://github.com/lightdarkmaster/github-readme-stats#common-options). You can turn off these rate limit protections by deploying [your own Vercel instance](#disable-rate-limit-protections).

<img alt="Uptime Badge" src="https://img.shields.io/endpoint?url=https%3A%2F%2Fgithub-readme-stats-git-monitoring-github-readme-stats-team.vercel.app%2Fapi%2Fstatus%2Fup%3Ftype%3Dshields">

> [!IMPORTANT]\
> We're a small team, and to prioritize, we rely on upvotes :+1:. We use the Top Issues dashboard for tracking community demand (see [#1935](https://github.com/lightdarkmaster/github-readme-stats/issues/1935)). Do not hesitate to upvote the issues and pull requests you are interested in. We will work on the most upvoted first.

# GitHub Stats Card

Copy and paste this into your markdown, and that's it. Simple!

Change the `?username=` value to your GitHub username.

```md
[![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster)](https://github.com/lightdarkmaster/github-readme-stats)
```

> [!WARNING]\
> By default, the stats card only shows statistics like stars, commits, and pull requests from public repositories. To show private statistics on the stats card, you should [deploy your own instance](#deploy-on-your-own) using your own GitHub API token.

> [!NOTE]\
> Available ranks are S (top 1%), A+ (12.5%), A (25%), A- (37.5%), B+ (50%), B (62.5%), B- (75%), C+ (87.5%) and C (everyone). This ranking scheme is based on the [Japanese academic grading](https://wikipedia.org/wiki/Academic_grading_in_Japan) system. The global percentile is calculated as a weighted sum of percentiles for each statistic (number of commits, pull requests, reviews, issues, stars, and followers), based on the cumulative distribution function of the [exponential](https://wikipedia.org/wiki/exponential_distribution) and the [log-normal](https://wikipedia.org/wiki/Log-normal_distribution) distributions. The implementation can be investigated at [src/calculateRank.js](https://github.com/lightdarkmaster/github-readme-stats/blob/master/src/calculateRank.js). The circle around the rank shows 100 minus the global percentile.

### Hiding individual stats

You can pass a query parameter `&hide=` to hide any specific stats with comma-separated values.

> Options: `&hide=stars,commits,prs,issues,contribs`

```md
![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster&hide=contribs,prs)
```

### Showing additional individual stats

You can pass a query parameter `&show=` to show any specific additional stats with comma-separated values.

> Options: `&show=reviews,discussions_started,discussions_answered,prs_merged,prs_merged_percentage`

```md
![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show=reviews,discussions_started,discussions_answered,prs_merged,prs_merged_percentage)
```

### Showing icons

To enable icons, you can pass `&show_icons=true` in the query param, like so:

```md
![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true)
```

### Themes

With inbuilt themes, you can customize the look of the card without doing any [manual customization](#customization).

Use `&theme=THEME_NAME` parameter like so :

```md
![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true&theme=radical)
```

#### All inbuilt themes

GitHub Readme Stats comes with several built-in themes (e.g. `dark`, `radical`, `merko`, `gruvbox`, `tokyonight`, `onedark`, `cobalt`, `synthwave`, `highcontrast`, `dracula`).

<img src="https://res.cloudinary.com/lightdarkmaster/image/upload/v1595174536/grs-themes_l4ynja.png" alt="GitHub Readme Stats Themes" width="600px"/>

You can look at a preview for [all available themes](themes/README.md) or checkout the [theme config file](themes/index.js). Please note that we paused the addition of new themes to decrease maintenance efforts; all pull requests related to new themes will be closed.

#### Responsive Card Theme

[![Christian's GitHub stats-Dark](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&show_icons=true\&theme=dark#gh-dark-mode-only)](https://github.com/lightdarkmaster/github-readme-stats#responsive-card-theme#gh-dark-mode-only)
[![Christian's GitHub stats-Light](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&show_icons=true\&theme=default#gh-light-mode-only)](https://github.com/lightdarkmaster/github-readme-stats#responsive-card-theme#gh-light-mode-only)

Since GitHub will re-upload the cards and serve them from their [CDN](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-anonymized-urls), we can not infer the browser/GitHub theme on the server side. There are, however, four methods you can use to create dynamics themes on the client side.

##### Use the transparent theme

We have included a `transparent` theme that has a transparent background. This theme is optimized to look good on GitHub's dark and light default themes. You can enable this theme using the `&theme=transparent` parameter like so:

```md
![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true&theme=transparent)
```

<details>
<summary>:eyes: Show example</summary>

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&show_icons=true\&theme=transparent)

</details>

##### Add transparent alpha channel to a themes bg\_color

You can use the `bg_color` parameter to make any of [the available themes](themes/README.md) transparent. This is done by setting the `bg_color` to a color with a transparent alpha channel (i.e. `bg_color=00000000`):

```md
![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true&bg_color=00000000)
```

<details>
<summary>:eyes: Show example</summary>

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&show_icons=true\&bg_color=00000000)

</details>

##### Use GitHub's theme context tag

You can use [GitHub's theme context](https://github.blog/changelog/2021-11-24-specify-theme-context-for-images-in-markdown/) tags to switch the theme based on the user GitHub theme automatically. This is done by appending `#gh-dark-mode-only` or `#gh-light-mode-only` to the end of an image URL. This tag will define whether the image specified in the markdown is only shown to viewers using a light or a dark GitHub theme:

```md
[![Christian's GitHub stats-Dark](https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true&theme=dark#gh-dark-mode-only)](https://github.com/lightdarkmaster/github-readme-stats#gh-dark-mode-only)
[![Christian's GitHub stats-Light](https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true&theme=default#gh-light-mode-only)](https://github.com/lightdarkmaster/github-readme-stats#gh-light-mode-only)
```

<details>
<summary>:eyes: Show example</summary>

[![Christian's GitHub stats-Dark](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&show_icons=true\&theme=dark#gh-dark-mode-only)](https://github.com/lightdarkmaster/github-readme-stats#gh-dark-mode-only)
[![Christian's GitHub stats-Light](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&show_icons=true\&theme=default#gh-light-mode-only)](https://github.com/lightdarkmaster/github-readme-stats#gh-light-mode-only)

</details>

##### Use GitHub's new media feature

You can use [GitHub's new media feature](https://github.blog/changelog/2022-05-19-specify-theme-context-for-images-in-markdown-beta/) in HTML to specify whether to display images for light or dark themes. This is done using the HTML `<picture>` element in combination with the `prefers-color-scheme` media feature.

```html
<picture>
  <source
    srcset="https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true&theme=dark"
    media="(prefers-color-scheme: dark)"
  />
  <source
    srcset="https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true"
    media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"
  />
  <img src="https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true" />
</picture>
```

<details>
<summary>:eyes: Show example</summary>

<picture>
  <source
    srcset="https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true&theme=dark"
    media="(prefers-color-scheme: dark)"
  />
  <source
    srcset="https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true"
    media="(prefers-color-scheme: light), (prefers-color-scheme: no-preference)"
  />
  <img src="https://github-readme-stats.vercel.app/api?username=lightdarkmaster&show_icons=true" />
</picture>

</details>

If we don't support your language, please consider contributing! You can find more information about how to do it in our [contributing guidelines](CONTRIBUTING.md#translations-contribution).

#### Stats Card Exclusive Options

| Name | Description | Type | Default value |
| --- | --- | --- | --- |
| `hide` | Hides the [specified items](#hiding-individual-stats) from stats. | string (comma-separated values) | `null` |
| `hide_title` | Hides the title of your stats card. | boolean | `false` |
| `card_width` | Sets the card's width manually. | number | `500px  (approx.)` |
| `hide_rank` | Hides the rank and automatically resizes the card width. | boolean | `false` |
| `rank_icon` | Shows alternative rank icon (i.e. `github`, `percentile` or `default`). | enum | `default` |
| `show_icons` | Shows icons near all stats. | boolean | `false` |
| `include_all_commits` | Count total commits instead of just the current year commits. | boolean | `false` |
| `line_height` | Sets the line height between text. | integer | `25` |
| `exclude_repo` | Excludes specified repositories. | string (comma-separated values) | `null` |
| `custom_title` | Sets a custom title for the card. | string | `<username> GitHub Stats` |
| `text_bold` | Uses bold text. | boolean | `true` |
| `disable_animations` | Disables all animations in the card. | boolean | `false` |
| `ring_color` | Color of the rank circle. | string (hex color) | `2f80ed` |
| `number_format` | Switches between two available formats for displaying the card values `short` (i.e. `6.6k`) and `long` (i.e. `6626`). | enum | `short` |
| `show` | Shows [additional items](#showing-additional-individual-stats) on stats card (i.e. `reviews`, `discussions_started`, `discussions_answered`, `prs_merged` or `prs_merged_percentage`). | string (comma-separated values) | `null` |

> [!NOTE]\
> When hide\_rank=`true`, the minimum card width is 270 px + the title length and padding.

#### Repo Card Exclusive Options

| Name | Description | Type | Default value |
| --- | --- | --- | --- |
| `show_owner` | Shows the repo's owner name. | boolean | `false` |
| `description_lines_count` | Manually set the number of lines for the description. Specified value will be clamped between 1 and 3. If this parameter is not specified, the number of lines will be automatically adjusted according to the actual length of the description. | number | `null` |

#### Gist Card Exclusive Options

| Name | Description | Type | Default value |
| --- | --- | --- | --- |
| `show_owner` | Shows the gist's owner name. | boolean | `false` |

#### Language Card Exclusive Options

| Name | Description | Type | Default value |
| --- | --- | --- | --- |
| `hide` | Hides the [specified languages](#hide-individual-languages) from card. | string (comma-separated values) | `null` |
| `hide_title` | Hides the title of your card. | boolean | `false` |
| `layout` | Switches between five available layouts `normal` & `compact` & `donut` & `donut-vertical` & `pie`. | enum | `normal` |
| `card_width` | Sets the card's width manually. | number | `300` |
| `langs_count` | Shows more languages on the card, between 1-20. | integer | `5` for `normal` and `donut`, `6` for other layouts |
| `exclude_repo` | Excludes specified repositories. | string (comma-separated values) | `null` |
| `custom_title` | Sets a custom title for the card. | string | `Most Used Languages` |
| `disable_animations` | Disables all animations in the card. | boolean | `false` |
| `hide_progress` | Uses the compact layout option, hides percentages, and removes the bars. | boolean | `false` |
| `size_weight` | Configures language stats algorithm (see [Language stats algorithm](#language-stats-algorithm)). | integer | `1` |
| `count_weight` | Configures language stats algorithm (see [Language stats algorithm](#language-stats-algorithm)). | integer | `0` |

> [!WARNING]\
> Language names should be URI-escaped, as specified in [Percent Encoding](https://en.wikipedia.org/wiki/Percent-encoding)
> (i.e: `c++` should become `c%2B%2B`, `jupyter notebook` should become `jupyter%20notebook`, etc.) You can use
> [urlencoder.org](https://www.urlencoder.org/) to help you do this automatically.

### Demo

![Gist Card](https://github-readme-stats.vercel.app/api/gist?id=bbfce31e0217a3689c8d961a356cb10d)

Use [show\_owner](#gist-card-exclusive-options) query option to include the gist's owner username

![Gist Card](https://github-readme-stats.vercel.app/api/gist?id=bbfce31e0217a3689c8d961a356cb10d\&show_owner=true)

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=lightdarkmaster)

*   Donut Chart layout

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=lightdarkmaster\&layout=donut)](https://github.com/lightdarkmaster/github-readme-stats)

*   Donut Vertical Chart layout

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=lightdarkmaster\&layout=donut-vertical)](https://github.com/lightdarkmaster/github-readme-stats)

*   Pie Chart layout

[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=lightdarkmaster\&layout=pie)](https://github.com/lightdarkmaster/github-readme-stats)

*   Hidden progress bars

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=lightdarkmaster\&hide_progress=true)


# All Demos

*   Default

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster)

*   Hiding specific stats

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&hide=contribs,issues)

*   Showing additional stats

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&show_icons=true\&show=reviews,discussions_started,discussions_answered,prs_merged,prs_merged_percentage)

*   Showing icons

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&hide=issues\&show_icons=true)

*   Shows Github logo instead rank level

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&rank_icon=github)

*   Shows user rank percentile instead of rank level

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&rank_icon=percentile)

*   Customize Border Color

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&border_color=2e4058)

*   Include All Commits

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&include_all_commits=true)

*   Themes

Choose from any of the [default themes](#themes)

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&show_icons=true\&theme=radical)

*   Gradient

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api?username=lightdarkmaster\&bg_color=30,e96443,904e95\&title_color=fff\&text_color=fff)

*   Customizing stats card

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api/?username=lightdarkmaster\&show_icons=true\&title_color=fff\&icon_color=79ff97\&text_color=9f9f9f\&bg_color=151515)

*   Setting card locale

![Christian's GitHub stats](https://github-readme-stats.vercel.app/api/?username=lightdarkmaster\&locale=es)

*   Customizing repo card

![Customized Card](https://github-readme-stats.vercel.app/api/pin?username=lightdarkmaster\&repo=github-readme-stats\&title_color=fff\&icon_color=f9f9f9\&text_color=9f9f9f\&bg_color=151515)

*   Gist card

![Gist Card](https://github-readme-stats.vercel.app/api/gist?id=bbfce31e0217a3689c8d961a356cb10d)

*   Customizing gist card

![Gist Card](https://github-readme-stats.vercel.app/api/gist?id=bbfce31e0217a3689c8d961a356cb10d&theme=calm)

*   Top languages

![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=lightdarkmaster)

## Quick Tip (Align The Cards)

By default, GitHub does not lay out the cards side by side. To do that, you can use this approach:

```html
<a href="https://github.com/lightdarkmaster/github-readme-stats">
  <img height=200 align="center" src="https://github-readme-stats.vercel.app/api?username=lightdarkmaster" />
</a>
<a href="https://github.com/lightdarkmaster/convoychat">
  <img height=200 align="center" src="https://github-readme-stats.vercel.app/api/top-langs?username=lightdarkmaster&layout=compact&langs_count=8&card_width=320" />
</a>
```

```html
<a href="https://github.com/lightdarkmaster/github-readme-stats">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=lightdarkmaster&repo=github-readme-stats" />
</a>
<a href="https://github.com/lightdarkmaster/convoychat">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=lightdarkmaster&repo=convoychat" />
</a>
```

<details>
<summary>:eyes: Show example</summary>

<a href="https://github.com/lightdarkmaster/github-readme-stats">
  <img height=200 align="center" src="https://github-readme-stats.vercel.app/api?username=lightdarkmaster" />
</a>
<a href="https://github.com/lightdarkmaster/convoychat">
  <img height=200 align="center" src="https://github-readme-stats.vercel.app/api/top-langs?username=lightdarkmaster&layout=compact&langs_count=8&card_width=320" />
</a>

***

<a href="https://github.com/lightdarkmaster/github-readme-stats">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=lightdarkmaster&repo=github-readme-stats" />
</a>
<a href="https://github.com/lightdarkmaster/convoychat">
  <img align="center" src="https://github-readme-stats.vercel.app/api/pin/?username=lightdarkmaster&repo=convoychat" />
</a>

</details>

# Deploy on your own

## On Vercel

### :film\_projector: [Check Out Step By Step Video Tutorial By @codeSTACKr](https://youtu.be/n6d4KHSKqGk?t=107)

Since the GitHub API only allows 5k requests per hour, my `https://github-readme-stats.vercel.app/api` could possibly hit the rate limiter. If you host it on your own Vercel server, then you do not have to worry about anything. Click on the deploy button to get started!

> [!NOTE]\
> Since [#58](https://github.com/lightdarkmaster/github-readme-stats/pull/58), we should be able to handle more than 5k requests and have fewer issues with downtime :grin:.

> [!NOTE]\
> If you are on the [Pro (i.e. paid)](https://vercel.com/pricing) Vercel plan, the [maxDuration](https://vercel.com/docs/concepts/projects/project-configuration#value-definition) value found in the [vercel.json](https://github.com/lightdarkmaster/github-readme-stats/blob/master/vercel.json) can be increased when your Vercel instance frequently times out during the card request. You are advised to keep this value lower than `30` seconds to prevent high memory usage.

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/lightdarkmaster/github-readme-stats)

<details>
 <summary><b>:hammer_and_wrench: Step-by-step guide on setting up your own Vercel instance</b></summary>

1.  Go to [vercel.com](https://vercel.com/).
2.  Click on `Log in`.
    ![](https://files.catbox.moe/pcxk33.png)
3.  Sign in with GitHub by pressing `Continue with GitHub`.
    ![](https://files.catbox.moe/b9oxey.png)
4.  Sign in to GitHub and allow access to all repositories if prompted.
5.  Fork this repo.
6.  Go back to your [Vercel dashboard](https://vercel.com/dashboard).
7.  To import a project, click the `Add New...` button and select the `Project` option.
    ![](https://files.catbox.moe/3n76fh.png)
8.  Click the `Continue with GitHub` button, search for the required Git Repository and import it by clicking the `Import` button. Alternatively, you can import a Third-Party Git Repository using the `Import Third-Party Git Repository ->` link at the bottom of the page.
    ![](https://files.catbox.moe/mg5p04.png)
9.  Create a personal access token (PAT) [here](https://github.com/settings/tokens/new) and enable the `repo` and `user` permissions (this allows access to see private repo and user stats).
10. Add the PAT as an environment variable named `PAT_1` (as shown).
    ![](https://files.catbox.moe/0yclio.png)
11. Click deploy, and you're good to go. See your domains to use the API!

</details>

## On other platforms

> [!WARNING]\
> This way of using GRS is not officially supported and was added to cater to some particular use cases where Vercel could not be used (e.g. [#2341](https://github.com/lightdarkmaster/github-readme-stats/discussions/2341)). The support for this method, therefore, is limited.

