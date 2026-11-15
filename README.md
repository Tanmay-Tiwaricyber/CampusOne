# CampusOne — One Campus. One Connected System.

A responsive single-page presentation for **CampusOne**, a student Design Thinking & Innovation project exploring a unified College ERP concept. The site is illustrative and does not implement the ERP workflows.

Awwwards-level retro-tech editorial style (v2): cream paper with faint grid + grain, oversized Inter Tight type with outlined accents, asymmetric layouts, OS-window cards, taped polaroids, sticky notes, rotating starburst, and a soft-blue retro CRT monitor as the hero object (using `monitor.png` / `monitor-opt.jpg`). Colour theme unchanged: cream `#F7F4EC`, cobalt `#2F5BFF`, periwinkle `#8FA6FF`, sky `#CFE0FF`, lavender `#EFEAFF`, charcoal `#1B1B22`.

Interactions: custom cursor, scroll progress, watermark parallax, magnetic buttons, 3D tilt cards, mouse-parallax monitor, animated roadmap fill, staggered reveals — all disabled under `prefers-reduced-motion`.

**3D clay assets (v3):** Generated with the shared style block (soft pastel clay, sky/cobalt/lavender/cream, isolated on cream) and optimized to `assets/opt/*.jpg` (~820 KB total). Coded CSS CRT monitors have been removed — all monitors are now real images:
- `assets/opt/hero-monitor.jpg` — dashboard monitor (hero + dashboards)
- `assets/opt/problem-monitor.jpg` — messy-windows monitor
- `assets/opt/timeline-monitor.jpg` — timeline monitor
- `assets/opt/smiley-monitor.jpg` — smiley monitor (CTA)
- `assets/opt/role-{student,parent,teacher,admin}.jpg` — role characters
- `assets/opt/team-{1,2}.jpg` — team avatars (third avatar + feature/security icons, props, OG banner and logo mark are queued for the next generation batch — image limit 10/turn)
- `monitor-transparent.webp` (54 KB) — original `monitor.png` with cream background made transparent

## Files

| File | Purpose |
|---|---|
| `index.html` | The entire site — HTML + CSS + JS in one file (~55 KB, zero build step) |
| `monitor.png` | Original 3D CRT monitor artwork (1448×1086) |
| `monitor-opt.jpg` | Web-optimized hero image (1200×900, ~77 KB) used by the page + Open Graph |
| `vercel.json` | Vercel config (clean URLs, security + cache headers) |

## Run locally

No build, no dependencies:

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

Or open `index.html` directly in a browser.

## Deploy on Vercel

**Option A — GitHub import (recommended):**
1. Push this repo to GitHub.
2. Go to [vercel.com/new](https://vercel.com/new) → Import `Tanmay-Tiwaricyber/CampusOne`.
3. Framework preset: **Other** (static site). Build command: *(empty)*. Output directory: *(empty / root)*.
4. Deploy. The site is live at `https://campusone.vercel.app` (or your project URL).

**Option B — Vercel CLI:**
```bash
npm i -g vercel
vercel --prod
```

**Option C — Drag & drop:** zip `index.html`, `monitor-opt.jpg`, `monitor.png`, `vercel.json` and drop the folder at [vercel.com](https://vercel.com).

> This repo is deployed via the Vercel connector as project `campusone`.

## Page structure (14 sections)

1. **Navbar** — sticky glass blur, `campusone.` logo, links, student-project tag, charcoal pill CTA, mobile hamburger.
2. **Hero** — giant `campusone` gradient watermark, pixel eyebrow, `one campus. one connected system.` headline, CRT monitor image flanked by sticky notes + project starburst, marquee strip.
3. **Problem** — `campus life runs on scattered systems.` + 3 sticky-note pains + messy overlapping-windows CRT.
4. **Solution** — `one platform. four roles.` + 4 polaroid role cards + configurable-roles line.
5. **Features bento** (pale lavender) — `everything has a status.` Document Vault flagship OS-window with animated status chips + 4 smaller cards.
6. **How it works** — `from request to resolved.` 4 numbered steps + hand-drawn squiggle + timeline CRT.
7. **Role dashboards** — pixel-font tabs (Student / Parent / Teacher / Admin), CRT dashboard mockup + 3 benefits per role.
8. **Security** (soft-blue gradient) — `built to be trusted.` 2×3 OS-window grid.
9. **Roadmap** — `built in phases.` 8-segment loading-bar timeline with pixel phase labels.
10. **Design thinking** — `designed with people, not for them.` 5-stage polaroid strip + key-insight sticky note.
11. **Team** — Tanmay Tiwari, Aditya Verma, Shivansh Dwivedi (B.Tech CSE AIML, MIPS) polaroids with placeholder avatars.
12. **FAQ** — 5 retro-window accordion rows.
13. **Project closing** — concept summary, smiley CRT, links to the design process and team, and marquee.
14. **Footer** (charcoal) — logo, tagline, links, `Made at Maharana Institute of Professional Studies`, `© 2026 CampusOne`.

## Design system

- **Colors:** cream `#F7F4EC`, periwinkle `#8FA6FF` → sky `#CFE0FF`, lavender `#EFEAFF`, cobalt `#2F5BFF`, charcoal `#1B1B22`. Accents (pink/lime/yellow) sparingly; status colors only on chips.
- **Type:** Inter Tight (headings, lowercase + period), Inter (body), JetBrains Mono (labels/eyebrows), Press Start 2P (pixel tags, sparingly).
- **Components:** OS-window cards (3 dots), polaroids, sticky notes (rotated), starburst sticker, squiggle SVG, charcoal pill buttons, 1px hairlines, 24px radius, soft shadows.
- **Motion:** gentle monitor float, sticky-note tilt, 4px card lift, fade-up on scroll (IntersectionObserver), slow marquee, blinking pixel cursor. All disabled under `prefers-reduced-motion`.
- **Rules respected:** ≤3 collage elements per section, 12-column grid, max-width 1200px, no stock photos, no neon, no emoji, WCAG AA contrast, visible focus states.

## Technical notes

- **Semantic HTML**, reusable component patterns (`Navbar`, `Hero`, `StickyNote`, `Polaroid`, `OSWindowCard`, `BentoCard`, `Marquee`, `Accordion`, `Tabs`) implemented as CSS classes + small JS renderers.
- **SEO:** meta description, Open Graph + Twitter cards (using `monitor-opt.jpg`), JSON-LD Organization schema, canonical URL.
- **Performance:** single file, no framework runtime, inline CSS/JS, optimized hero image with `fetchpriority="high"`, system-friendly fonts with `display=swap` — Lighthouse 90+ ready.
- **Accessibility:** skip link, ARIA tabs/accordion, focus-visible rings, reduced-motion support.

### Next.js mapping

This static build mirrors a Next.js + Tailwind + Framer Motion implementation 1:1 — each section is a component (`components/Navbar.tsx`, `Hero.tsx`, `StickyNote.tsx`, `Polaroid.tsx`, `OSWindowCard.tsx`, `BentoCard.tsx`, `Marquee.tsx`, `Accordion.tsx`, `Tabs.tsx`), Tailwind tokens map to the CSS variables in `:root`, and Framer Motion `whileInView` maps to the IntersectionObserver reveal. The single-file version was chosen for instant Vercel deployment and a 90+ Lighthouse score with zero build time.

## Team

Tanmay Tiwari · Aditya Verma · Shivansh Dwivedi — B.Tech CSE (AIML), Maharana Institute of Professional Studies.

## Student sign-in demo

`auth.html` provides a client-side sample login for the single student account supplied for this project, which opens `student.html` with illustrative data. The browser session flag supports the demo flow and sign-out only: **it is not authentication or authorization**, the sample credentials are visible in page source, and the dashboard must not contain real data. Other roles and automatic role detection are not implemented. Before any real deployment, replace the demo with a secure identity provider, protected server-side sessions, and server-enforced role and record-level access checks. Never use real passwords or personal information in this static demo.
