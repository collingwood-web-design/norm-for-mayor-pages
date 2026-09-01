# -*- coding: utf-8 -*-
"""Build vision-pp03.html from PP04 shell + PP03 Word content."""
import re
from pathlib import Path

ROOT = Path(r"d:\NEW CLIENTS\NORM")
base = (ROOT / "vision-pp04.html").read_text(encoding="utf-8")

head = base[: base.index('<main id="main-content"')]
footer = base[base.index('<footer class="site-footer"'):]

replacements = [
    (
        "PP04: Building a Financially Sustainable Collingwood. Smart budgeting and fiscal responsibility in Norm Sandberg's Vision for Collingwood.",
        "PP03: Downtown Parking, Housing and Commercial Catalyst Project. Making better use of Collingwood's downtown municipal parking lots.",
    ),
    (
        "PP04 Building a Financially Sustainable Collingwood | Vision for Collingwood | Norm Sandberg",
        "PP03 Downtown Parking, Housing & Commercial Catalyst | Vision for Collingwood | Norm Sandberg",
    ),
    ("vision-pp04.html", "vision-pp03.html"),
    (
        'content="PP04: Building a Financially Sustainable Collingwood. Smart budgeting and fiscal responsibility in Norm Sandberg\'s Vision for Collingwood."',
        'content="PP03: Downtown Parking, Housing and Commercial Catalyst Project. More parking, workforce housing and commercial space on municipal land we already own."',
    ),
    (
        "pp04-financially-sustainable.jpg",
        "vision-hero.jpg",
    ),
    (
        "Cover image for PP04: Building a Financially Sustainable Collingwood - Norm Sandberg Vision for Collingwood",
        "Downtown Collingwood representing PP03 Parking, Housing and Commercial Catalyst Project",
    ),
    ("Building a Financially Sustainable Collingwood", "Downtown Parking, Housing & Commercial Catalyst Project"),
    (
        "Responsible financial management, asset renewal and smart investment.",
        "More parking. More workforce housing. More commercial space.",
    ),
    ("page-policy--pp04", "page-policy--pp03"),
    ('content="Building a Financially Sustainable Collingwood"', 'content="Downtown Parking, Housing & Commercial Catalyst Project"'),
    ('"alternativeHeadline": "PP04"', '"alternativeHeadline": "PP03"'),
    ('"dateModified": "2026-08-07"', '"dateModified": "2026-09-01"'),
]

for old, new in replacements:
    head = head.replace(old, new)

head = re.sub(
    r"<title>.*?</title>",
    "<title>PP03 Downtown Parking, Housing &amp; Commercial Catalyst | Vision for Collingwood | Norm Sandberg</title>",
    head,
    count=1,
)

main = r'''      <main id="main-content" itemprop="mainContentOfPage" itemscope itemtype="https://schema.org/Article">
        <meta itemprop="headline" content="Downtown Parking, Housing &amp; Commercial Catalyst Project" />
        <meta itemprop="description" content="PP03: Downtown Parking, Housing and Commercial Catalyst Project. Making better use of Collingwood's downtown municipal parking lots." />
        <meta itemprop="inLanguage" content="en-CA" />
        <div itemprop="author" itemscope itemtype="https://schema.org/Person">
          <meta itemprop="name" content="Norm Sandberg" />
          <link itemprop="url" href="https://normformayor.ca/" />
        </div>

        <header class="policy-hero">
          <div class="policy-hero__media" aria-hidden="true">
            <img
              itemprop="image"
              src="https://media.cwd-cdn.com/norm-for-mayor/vision/vision-hero.jpg"
              alt="Downtown Collingwood representing PP03: Parking, Housing and Commercial Catalyst Project"
              width="1600"
              height="427"
              loading="eager"
              decoding="async"
            />
          </div>
          <div class="policy-hero__overlay">
            <div class="container policy-hero__content">
              <p class="policy-hero__eyebrow">PP03</p>
              <h1 class="policy-hero__title" itemprop="headline">Downtown Parking, Housing &amp; Commercial Catalyst Project</h1>
              <p class="policy-hero__lead">Making better use of Collingwood&rsquo;s downtown municipal parking lots &mdash; more parking, more workforce housing, more commercial space.</p>
            </div>
          </div>
        </header>

        <div class="policy-doc">
          <div class="container">

            <section class="policy-sheet" aria-labelledby="why-matters-heading">
              <div class="policy-sheet__copy">
                <h2 id="why-matters-heading">Why This Matters</h2>
                <p>For decades, Collingwood has talked about three related downtown challenges: the need for more public parking, the shortage of housing for people who work in our community, and the importance of maintaining a strong and vibrant commercial core.</p>
                <p>At the same time, the Town owns strategically located downtown properties that currently serve essentially one purpose &mdash; surface parking.</p>
                <p>I believe we should ask a simple question: can these publicly owned properties work harder for our community?</p>
                <p>The planning work I have undertaken suggests they can.</p>
              </div>

              <aside class="policy-sheet__principle">
                <p><strong>Guiding Principle:</strong> Public land should deliver more than one benefit. Parking, housing and commercial space can work together when they are planned as one project.</p>
              </aside>

              <div class="policy-sheet__tri">
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">01</span>
                  <h3>More Parking</h3>
                  <p>Structured parking creates an opportunity to increase public parking while using the space above and around it for other community needs.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">02</span>
                  <h3>Workforce Housing</h3>
                  <p>Employers struggle with the availability and cost of housing for the people who work here. Downtown municipal land may help address that shortage.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">03</span>
                  <h3>Commercial Vitality</h3>
                  <p>New street-level commercial space can support downtown businesses, tourism, community events and year-round activity.</p>
                </article>
              </div>
            </section>

            <p class="policy-doc__source">Vision for Collingwood &mdash; Publication No. 3: Downtown Parking, Housing &amp; Commercial Catalyst Project.</p>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP03</span>
              <div class="policy-doc__banner-text">
                <h2>The Opportunity</h2>
                <p>Preliminary concepts for two municipal parking lots show real promise</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="opportunity-heading">
              <h2 id="opportunity-heading" class="sr-only">The Opportunity</h2>
              <div class="policy-sheet__copy">
                <p>Preliminary concepts for the municipal parking lots at <strong>140 Ste. Marie Street</strong> and <strong>Second Street/Pine Street</strong> demonstrate the potential to replace surface parking with carefully designed mixed-use developments providing substantially more public parking, new workforce and market rental apartments, and new street-level commercial space &mdash; while retaining these important properties in municipal ownership.</p>
                <p>These are concepts, not approved projects. They require independent review by Town staff and qualified planning, architectural, engineering, financial and legal professionals.</p>
                <p>But the work has advanced far enough to show real promise. I believe the next Council should determine whether these opportunities can be advanced through appropriate public/private partnerships.</p>
              </div>
            </section>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP03</span>
              <div class="policy-doc__banner-text">
                <h2>Making Public Land Work Harder</h2>
                <p>Surface parking is an inefficient use of valuable downtown land</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="public-land-heading">
              <h2 id="public-land-heading" class="sr-only">Making Public Land Work Harder</h2>
              <div class="policy-sheet__copy">
                <p>Surface parking is an inefficient use of valuable downtown land. Structured parking creates an opportunity to increase parking while using the space above and around it for other community needs.</p>
                <p>Parking remains essential downtown infrastructure. It supports businesses, restaurants, tourism, community events, cultural activities and the Eddie Bush Memorial Arena.</p>
                <p>The opportunity is to provide <strong>more parking &mdash; not less</strong> &mdash; while also creating housing and commercial activity on the same municipal land.</p>
                <p>The work completed since this initiative was first announced demonstrates what that could mean.</p>
              </div>
            </section>

            <section class="policy-site" aria-labelledby="ste-marie-heading">
              <div class="policy-site__header">
                <h3 id="ste-marie-heading">140 Ste. Marie Street</h3>
              </div>
              <div class="policy-site__body">
                <div>
                  <div class="policy-sheet__copy">
                    <p>The 140 Ste. Marie Street concept has been developed through a detailed planning-level project development study.</p>
                    <p>The existing municipal surface lot contains <strong>87 public parking stalls</strong>.</p>
                    <p>The concept provides <strong>196 structured parking stalls</strong> &mdash; 181 public and 15 residential &mdash; producing <strong>94 net new public parking stalls</strong>.</p>
                    <p>It also provides <strong>30 rental apartments</strong>:</p>
                    <ul>
                      <li>22 workforce rental apartments: 8 studios, 10 one-bedroom and 4 two-bedroom;</li>
                      <li>8 market rental apartments: 4 two-bedroom and 4 fourth-floor penthouses.</li>
                    </ul>
                    <p>At street level, approximately <strong>7,300 square feet</strong> of new commercial space is accommodated in five storefronts facing Ste. Marie Street.</p>
                    <p>The building concept has also been developed to respond to Collingwood&rsquo;s Downtown Heritage Conservation District, including an active street frontage and recessed fourth floor.</p>
                    <p>The planning work suggests that a public/private partnership warrants further investigation while allowing the Town to retain ownership of this strategic property.</p>
                  </div>
                  <table class="policy-data-table">
                    <caption>140 Ste. Marie &mdash; At a Glance</caption>
                    <thead>
                      <tr>
                        <th scope="col"></th>
                        <th scope="col" class="policy-data-table__col-head">Existing</th>
                        <th scope="col" class="policy-data-table__col-head">Concept</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row">Public parking</th>
                        <td>87</td>
                        <td>181</td>
                      </tr>
                      <tr>
                        <th scope="row">Residential parking</th>
                        <td>&mdash;</td>
                        <td>15</td>
                      </tr>
                      <tr>
                        <th scope="row">Total parking</th>
                        <td>87</td>
                        <td>196</td>
                      </tr>
                      <tr class="policy-data-table__highlight">
                        <th scope="row">Net new public parking</th>
                        <td>&mdash;</td>
                        <td>+94</td>
                      </tr>
                      <tr>
                        <th scope="row">Rental apartments</th>
                        <td>0</td>
                        <td>30</td>
                      </tr>
                      <tr>
                        <th scope="row">Workforce / Market</th>
                        <td>&mdash;</td>
                        <td>22 / 8</td>
                      </tr>
                      <tr>
                        <th scope="row">Commercial space</th>
                        <td>0</td>
                        <td>&asymp;7,300 sq. ft.</td>
                      </tr>
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            <section class="policy-site" aria-labelledby="second-pine-heading">
              <div class="policy-site__header">
                <h3 id="second-pine-heading">Second Street / Pine Street</h3>
              </div>
              <div class="policy-site__body">
                <div>
                  <div class="policy-sheet__copy">
                    <p>The larger Second Street/Pine Street municipal lot demonstrates that the same approach may have even greater potential.</p>
                    <p>The current concept provides <strong>232 structured parking stalls</strong> &mdash; 217 public and 15 residential &mdash; compared with the 87 existing surface stalls used as the concept baseline. That represents approximately <strong>130 net new public parking stalls</strong>.</p>
                    <p>The concept also provides <strong>42 rental apartments</strong>:</p>
                    <ul>
                      <li>8 studios of approximately 500 sq. ft.;</li>
                      <li>20 one-bedroom apartments of approximately 600 sq. ft.;</li>
                      <li>8 two-bedroom apartments of approximately 700 sq. ft.; and</li>
                      <li>6 fourth-floor penthouse apartments.</li>
                    </ul>
                    <p>The apartments provide a combination of workforce and market rental housing, with the penthouses providing a market component that helps support a mixed-income development.</p>
                    <p>Approximately <strong>11,892 square feet</strong> of ground-floor commercial space would activate the Second and Pine Street frontages.</p>
                    <p>The concept also incorporates a new <strong>12 ft. &times; 30 ft. municipal bus depot</strong> with two washrooms, integrating another municipal function into the development rather than requiring a separate downtown property.</p>
                    <p>The concept uses heritage-inspired storefronts and masonry, traditional downtown proportions and a recessed fourth floor to demonstrate that structured parking and new development can be designed to complement the downtown rather than overwhelm it.</p>
                  </div>
                  <table class="policy-data-table">
                    <caption>Second / Pine &mdash; At a Glance</caption>
                    <thead>
                      <tr>
                        <th scope="col"></th>
                        <th scope="col" class="policy-data-table__col-head">Existing*</th>
                        <th scope="col" class="policy-data-table__col-head">Concept</th>
                      </tr>
                    </thead>
                    <tbody>
                      <tr>
                        <th scope="row">Public parking</th>
                        <td>87</td>
                        <td>217</td>
                      </tr>
                      <tr>
                        <th scope="row">Residential parking</th>
                        <td>&mdash;</td>
                        <td>15</td>
                      </tr>
                      <tr>
                        <th scope="row">Total parking</th>
                        <td>87</td>
                        <td>232</td>
                      </tr>
                      <tr class="policy-data-table__highlight">
                        <th scope="row">Net new public parking</th>
                        <td>&mdash;</td>
                        <td>+130</td>
                      </tr>
                      <tr>
                        <th scope="row">Rental apartments</th>
                        <td>0</td>
                        <td>42</td>
                      </tr>
                      <tr>
                        <th scope="row">Commercial space</th>
                        <td>0</td>
                        <td>&asymp;11,892 sq. ft.</td>
                      </tr>
                    </tbody>
                  </table>
                  <p class="policy-doc__source">*Existing-stall baseline to be confirmed through municipal due diligence.</p>
                </div>
              </div>
            </section>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP03</span>
              <div class="policy-doc__banner-text">
                <h2>What Could Two Municipal Properties Deliver?</h2>
                <p>We do not have to choose between parking, housing and commercial development</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="combined-heading">
              <h2 id="combined-heading" class="sr-only">Combined Potential</h2>
              <div class="policy-sheet__copy">
                <p>Together, these two planning concepts demonstrate the potential for substantially more public benefit from land the Town already owns &mdash; without necessarily selling the land.</p>
              </div>
              <div class="policy-potential" role="list" aria-label="Combined potential of both municipal properties">
                <div class="policy-potential__item" role="listitem">
                  <span class="policy-potential__value">428</span>
                  <span class="policy-potential__label">Structured parking stalls</span>
                </div>
                <div class="policy-potential__item" role="listitem">
                  <span class="policy-potential__value">398</span>
                  <span class="policy-potential__label">Public parking stalls</span>
                </div>
                <div class="policy-potential__item" role="listitem">
                  <span class="policy-potential__value">&asymp;224</span>
                  <span class="policy-potential__label">Net new public parking</span>
                </div>
                <div class="policy-potential__item" role="listitem">
                  <span class="policy-potential__value">72</span>
                  <span class="policy-potential__label">Rental apartments</span>
                </div>
                <div class="policy-potential__item" role="listitem">
                  <span class="policy-potential__value">&asymp;19,200</span>
                  <span class="policy-potential__label">Sq. ft. commercial space</span>
                </div>
              </div>
            </section>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP03</span>
              <div class="policy-doc__banner-text">
                <h2>A Public/Private Partnership &mdash; Not a Blank Cheque</h2>
                <p>Planning-level demonstrations of an opportunity worth investigating</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="partnership-heading">
              <h2 id="partnership-heading" class="sr-only">A Public/Private Partnership</h2>
              <div class="policy-sheet__split policy-sheet__split--issue">
                <div class="policy-sheet__stack">
                  <article>
                    <h3>Not a Residential Developer</h3>
                    <p>I am not proposing that the Town become a residential developer or commercial landlord. The model that should be investigated is a partnership in which the Town retains ownership of the land and municipal parking, while a private-sector partner develops and operates the residential and commercial components.</p>
                  </article>
                  <article>
                    <h3>Independent Professional Review</h3>
                    <p>The appropriate structure would have to be established through independent professional analysis and a transparent competitive process. That review must examine construction costs, financing, parking operations, housing economics, commercial demand, risk allocation, long-term land value and potential federal and provincial funding programs.</p>
                  </article>
                  <article>
                    <h3>No Assumed Grants</h3>
                    <p>No government grant should be assumed until it is secured. These concepts should therefore be viewed for what they are: planning-level demonstrations of an opportunity worth investigating.</p>
                  </article>
                </div>
                <aside class="policy-sheet__framework" aria-label="Partnership review requirements">
                  <h3>Review Must Examine</h3>
                  <ol>
                    <li><strong>Technical Viability</strong> Planning, architectural and engineering feasibility.</li>
                    <li><strong>Financial Viability</strong> Construction costs, financing and parking operations.</li>
                    <li><strong>Market Demand</strong> Housing economics and commercial demand downtown.</li>
                    <li><strong>Risk &amp; Value</strong> Risk allocation and long-term land value for taxpayers.</li>
                    <li><strong>Funding</strong> Potential federal and provincial programs &mdash; only if secured.</li>
                    <li><strong>Partnership Models</strong> Appropriate public/private structures with Town ownership retained.</li>
                    <li><strong>Public Process</strong> Consultation with downtown businesses and the community.</li>
                  </ol>
                </aside>
              </div>
            </section>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP03</span>
              <div class="policy-doc__banner-text">
                <h2>My Position</h2>
                <p>Enough promise to warrant the next step</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="position-heading">
              <h2 id="position-heading" class="sr-only">My Position</h2>
              <div class="policy-sheet__duo">
                <article>
                  <h3>Why Act Now</h3>
                  <p>Collingwood owns valuable downtown land that has performed essentially the same single function for decades. Meanwhile, we continue to hear about downtown parking. Employers struggle with the availability and cost of housing for the people who work here. Downtown businesses need customers and year-round activity. And taxpayers expect the Town to use public assets wisely.</p>
                  <p>The concepts developed for 140 Ste. Marie Street and Second Street/Pine Street show enough promise to warrant the next step.</p>
                </article>
                <article>
                  <h3>As Mayor, I Would Ask Council To</h3>
                  <ul>
                    <li>Direct Town staff and qualified consultants to independently determine technical, financial and market viability;</li>
                    <li>Examine appropriate public/private partnership models;</li>
                    <li>Consult with the downtown business community and the public;</li>
                    <li>Report back to Council before any decision is made to proceed.</li>
                  </ul>
                  <p>The work completed so far does not prove that every detail will work. It demonstrates enough potential to justify finding out.</p>
                </article>
              </div>

              <p class="policy-callout">
                Our downtown municipal land belongs to the people of Collingwood.
                <span class="policy-callout__sub">Let&rsquo;s find out whether it can work harder for them.<br />More parking. More workforce housing. More commercial space. A stronger downtown &mdash; using land we already own.</span>
              </p>
            </section>

            <div class="policy-sheet__duo">
              <article>
                <h3>Connecting the Vision</h3>
                <p>This publication complements <a class="policy-ref" href="vision-pp04.html">PP04</a> on financial sustainability, <a class="policy-ref" href="vision-pp05.html">PP05</a> on downtown mobility and parking management, and <a class="policy-ref" href="vision-pp07.html">PP07</a> on housing for a growing Collingwood.</p>
              </article>
              <article>
                <h3>Continuing the Conversation</h3>
                <p>Vision for Collingwood is intended to start conversations &mdash; not end them. Constructive comments, additional ideas and alternative perspectives are welcome as this vision continues to be refined.</p>
              </article>
            </div>

          </div>
        </div>

        <nav class="policy-pager policy-pager--footer" aria-label="Policy papers">
          <div class="container policy-pager__inner">
            <a class="policy-pager__link policy-pager__link--prev" href="vision-pp02.html">
              <span class="policy-pager__dir">Previous</span>
              <span class="policy-pager__label">PP02 Leadership Through Consensus</span>
            </a>
            <a class="policy-pager__all" href="vision-for-collingwood.html">ALL PAPERS</a>
            <a class="policy-pager__link policy-pager__link--next" href="vision-pp04.html">
              <span class="policy-pager__dir">Next</span>
              <span class="policy-pager__label">PP04 Financial Sustainability</span>
            </a>
          </div>
        </nav>
      </main>

'''

(ROOT / "vision-pp03.html").write_text(head + main + footer, encoding="utf-8")
print("Wrote vision-pp03.html")
