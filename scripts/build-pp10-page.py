# -*- coding: utf-8 -*-
"""Build vision-pp10.html from PP08 shell + PP10 Word content."""
import re
from pathlib import Path

ROOT = Path(r"d:\NEW CLIENTS\NORM")
base = (ROOT / "vision-pp08.html").read_text(encoding="utf-8")

head = base[: base.index('<main id="main-content"')]
footer = base[base.index('<footer class="site-footer"'):]

replacements = [
    (
        "PP08: Growing Opportunity - supporting business, strengthening partnerships and building prosperity so people can live, work, invest and build careers in Collingwood.",
        "PP10: Leading Collingwood Forward - experienced, practical and collaborative leadership. A clear plan, a strong team and a bright future for Collingwood.",
    ),
    (
        "PP08 Growing Opportunity | Vision for Collingwood | Norm Sandberg",
        "PP10 Leading Collingwood Forward | Vision for Collingwood | Norm Sandberg",
    ),
    ("vision-pp08.html", "vision-pp10.html"),
    (
        'content="PP08: Growing Opportunity - supporting business, strengthening partnerships and building prosperity so people can live, work, invest and build careers in Collingwood."',
        'content="PP10: Leading Collingwood Forward - experienced, practical and collaborative leadership for Collingwood."',
    ),
    (
        "pp08-growing-opportunity.jpg",
        "vision-hero.jpg",
    ),
    (
        "Downtown Collingwood patios, shops and cyclists representing PP08 Growing Opportunity",
        "Collingwood waterfront and community representing PP10 Leading Collingwood Forward",
    ),
    (
        "PP08 Growing Opportunity",
        "PP10 Leading Collingwood Forward",
    ),
    ("Growing Opportunity", "Leading Collingwood Forward"),
    (
        "Supporting business, strengthening partnerships and building prosperity.",
        "A clear plan. A strong team. A bright future.",
    ),
    ("page-policy--pp08", "page-policy--pp10"),
    ('content="Growing Opportunity"', 'content="Leading Collingwood Forward"'),
    ('content="PP08"', 'content="PP10"'),
    ('"alternativeHeadline": "PP08"', '"alternativeHeadline": "PP10"'),
    ('"dateModified": "2026-08-07"', '"dateModified": "2026-09-01"'),
]

for old, new in replacements:
    head = head.replace(old, new)

head = re.sub(
    r"<title>.*?</title>",
    "<title>PP10 Leading Collingwood Forward | Vision for Collingwood | Norm Sandberg</title>",
    head,
    count=1,
)

main = r'''      <main id="main-content" itemprop="mainContentOfPage" itemscope itemtype="https://schema.org/Article">
        <meta itemprop="headline" content="Leading Collingwood Forward" />
        <meta itemprop="description" content="PP10: Leading Collingwood Forward - experienced, practical and collaborative leadership for Collingwood." />
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
              alt="Collingwood waterfront and community representing PP10: Leading Collingwood Forward"
              width="1600"
              height="427"
              loading="eager"
              decoding="async"
            />
          </div>
          <div class="policy-hero__overlay">
            <div class="container policy-hero__content">
              <p class="policy-hero__eyebrow">PP10</p>
              <h1 class="policy-hero__title" itemprop="headline">Leading Collingwood Forward</h1>
              <p class="policy-hero__lead">A clear plan. A strong team. A bright future.</p>
            </div>
          </div>
        </header>

        <div class="policy-doc">
          <div class="container">

            <section class="policy-sheet" aria-labelledby="leadership-matters-heading">
              <div class="policy-sheet__copy">
                <h2 id="leadership-matters-heading">Leadership Matters</h2>
                <p>Collingwood is entering an important period in its history. We are growing. Our infrastructure must keep pace. Housing is increasingly difficult for the people who work in our community. Transportation pressures are increasing. Our downtown needs more parking, workforce housing and commercial opportunities. Municipal infrastructure must be maintained and renewed &mdash; while respecting the ability of taxpayers to pay.</p>
                <p>These are significant challenges. They are also opportunities.</p>
                <p>I believe Collingwood needs experienced, practical and collaborative leadership &mdash; leadership that understands municipal government, respects professional staff, welcomes different points of view and knows how to turn good ideas into achievable projects.</p>
              </div>

              <aside class="policy-sheet__principle">
                <p><strong>My Commitment:</strong> Listen carefully. Plan intelligently. Spend responsibly. Work collaboratively. Deliver results.</p>
              </aside>

              <div class="policy-sheet__tri">
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">01</span>
                  <h3>Growth With Discipline</h3>
                  <p>Collingwood should be ambitious about its future &mdash; but ambition must be matched by discipline, evidence and sound financial planning.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">02</span>
                  <h3>Practical Experience</h3>
                  <p>Leadership that understands municipal government, infrastructure, project delivery and the importance of long-term financial planning.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">03</span>
                  <h3>Collaborative Council</h3>
                  <p>A Mayor who establishes a respectful tone, encourages open debate and helps Council find common ground when opinions differ.</p>
                </article>
              </div>
            </section>

            <p class="policy-doc__source">Vision for Collingwood &mdash; Publication No. 10: Leading Collingwood Forward.</p>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP10</span>
              <div class="policy-doc__banner-text">
                <h2>Experience Matters</h2>
                <p>Turning good ideas into achievable projects</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="experience-heading">
              <h2 id="experience-heading" class="sr-only">Experience Matters</h2>
              <div class="policy-sheet__split policy-sheet__split--issue">
                <div class="policy-sheet__stack">
                  <article>
                    <h3>A Career in Municipal Infrastructure</h3>
                    <p>For more than 30 years, my professional career has involved working with municipalities across Ontario on the study, planning, design, funding and delivery of municipal infrastructure.</p>
                  </article>
                  <article>
                    <h3>From Idea to Delivery</h3>
                    <p>As a Certified Engineering Technologist, I have worked with municipal councils and staff, provincial and federal agencies, consultants, contractors, utilities, property owners and the public. Today, I manage engineering professionals and consultants working on an infrastructure program valued at approximately $500&nbsp;million.</p>
                  </article>
                  <article>
                    <h3>A Good Idea Is Only the Beginning</h3>
                    <p>Someone must determine whether it can be built, what it will cost, how it will be funded, what risks must be managed and how the project will be delivered. That is the practical experience I will bring to the Mayor&rsquo;s office.</p>
                  </article>
                </div>
                <aside class="policy-sheet__framework" aria-label="Leadership experience">
                  <h3>Leadership Experience</h3>
                  <ol>
                    <li><strong>Four Terms on Council</strong> Participating in initiatives that helped shape our community.</li>
                    <li><strong>Chair, Ontario Small Urban Municipalities</strong> Advocating for communities like Collingwood at the provincial level.</li>
                    <li><strong>President, Association of Municipalities of Ontario</strong> Building relationships across Ontario&rsquo;s municipal sector.</li>
                    <li><strong>Strong Advocate</strong> As Mayor, I will be a strong advocate for Collingwood at County, provincial, federal and private-sector tables.</li>
                  </ol>
                </aside>
              </div>
            </section>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP10</span>
              <div class="policy-doc__banner-text">
                <h2>Collaborative Leadership</h2>
                <p>Bringing people together to accomplish something</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="collaborative-heading">
              <h2 id="collaborative-heading" class="sr-only">Collaborative Leadership</h2>
              <div class="policy-sheet__copy">
                <p>A Mayor does not govern alone. Residents elect nine members of Council because no single person has all the answers. Each member brings different experiences, ideas and perspectives. Those differences should strengthen our decisions, not divide us.</p>
                <p>I believe in collaborative leadership, not command-and-control government. The Mayor should establish a respectful tone, encourage open debate, ensure Council has the information it needs and help find common ground when opinions differ.</p>
                <p>That does not mean avoiding difficult decisions. Leadership sometimes requires choices that will not please everyone. But residents should always be able to understand why a decision was made, what evidence supported it, what it will cost and what Council expects it to accomplish.</p>
                <p>Council establishes policy and priorities. Professional staff provide advice and implement Council&rsquo;s direction. The Mayor must help those responsibilities work effectively together.</p>
              </div>

              <aside class="policy-sheet__principle">
                <p><strong>Guiding Principle:</strong> The strongest Mayor is not the one who exercises the most authority. It is the one who can bring people together to accomplish something.</p>
              </aside>

              <div class="policy-sheet__quad">
                <div>
                  <h4>Questions Welcome</h4>
                  <p>Council should debate openly with the information it needs to decide.</p>
                </div>
                <div>
                  <h4>Staff Respected</h4>
                  <p>Professional expertise should inform policy and implementation.</p>
                </div>
                <div>
                  <h4>Residents Heard</h4>
                  <p>Residents must remain part of the conversation on major decisions.</p>
                </div>
                <div>
                  <h4>Disagreement Respectful</h4>
                  <p>Different perspectives should strengthen decisions, not divide Council.</p>
                </div>
              </div>
            </section>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP10</span>
              <div class="policy-doc__banner-text">
                <h2>Fiscal Responsibility</h2>
                <p>Getting the greatest long-term value from every dollar we spend</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="fiscal-heading">
              <h2 id="fiscal-heading" class="sr-only">Fiscal Responsibility</h2>
              <div class="policy-sheet__copy">
                <p>Every policy position in my Vision for Collingwood has one thing in common: someone has to pay for it. Taxpayers deserve a Council that never forgets that.</p>
                <p>Fiscal responsibility does not mean automatically saying no to spending. Municipalities must invest in roads, water and wastewater systems, parks, recreation, public facilities and the services residents rely upon. The question is whether we are spending wisely and receiving good value for every public dollar.</p>
              </div>

              <div class="policy-sheet__plan">
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">01</span>
                  <h3>Protect Taxpayers</h3>
                  <p>Support responsible and predictable financial planning that respects the ability of taxpayers to pay.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">02</span>
                  <h3>Build on Existing Plans</h3>
                  <p>Use Collingwood&rsquo;s long-term financial, asset-management and capital plans as the foundation for decisions.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">03</span>
                  <h3>Zero-Based Budgeting</h3>
                  <p>Gradually introduce zero-based budgeting principles, requiring programs to demonstrate continuing need and value.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">04</span>
                  <h3>Lifecycle Costs</h3>
                  <p>Consider the full lifecycle cost of municipal assets &mdash; not simply the initial construction price.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">05</span>
                  <h3>Growth Pays Its Way</h3>
                  <p>Ensure growth contributes appropriately toward the infrastructure it requires.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">06</span>
                  <h3>Strategic Debt</h3>
                  <p>Use municipal debt carefully and strategically for investments that deliver long-term value.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">07</span>
                  <h3>Pursue Shared Funding</h3>
                  <p>Aggressively pursue provincial and federal funding so Collingwood taxpayers do not carry costs that can appropriately be shared.</p>
                </article>
              </div>

              <div class="policy-sheet__duo">
                <article>
                  <h3>Being Prepared Matters</h3>
                  <p>My professional career has involved helping municipalities plan infrastructure, develop funding strategies and secure government assistance. When funding programs are announced, municipalities with well-developed priorities and projects are better positioned to compete successfully.</p>
                </article>
                <article>
                  <h3>Policy Position</h3>
                  <p>Fiscal responsibility is not about doing nothing. It is about getting the greatest long-term value from every dollar we spend &mdash; and ensuring every Council commitment can be delivered within a sound financial framework.</p>
                </article>
              </div>
            </section>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP10</span>
              <div class="policy-doc__banner-text">
                <h2>Making Town Hall Work Efficiently</h2>
                <p>Modern, effective and cost-conscious governance for Collingwood</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="town-hall-heading">
              <h2 id="town-hall-heading" class="sr-only">Making Town Hall Work Efficiently</h2>
              <div class="policy-sheet__split policy-sheet__split--issue">
                <div class="policy-sheet__stack">
                  <article>
                    <h3>Periodic Organizational Review</h3>
                    <p>Every successful organization should review its structure, responsibilities, processes and service-delivery methods from time to time. Municipal government should be no different. Collingwood has grown. Technology has changed. Community expectations have changed.</p>
                  </article>
                  <article>
                    <h3>First 100 Days Initiative</h3>
                    <p>With the support of Council, I will initiate a comprehensive organizational review within the first 100 days of the new term. The review should identify what is working well and where improvements may be possible.</p>
                  </article>
                  <article>
                    <h3>No Predetermined Cuts</h3>
                    <p>This will not begin with predetermined conclusions or arbitrary cuts. The objective is to preserve our strengths, identify weaknesses and opportunities, modernize where appropriate and ensure Collingwood has the most efficient, effective and cost-conscious governance model possible.</p>
                  </article>
                </div>
                <aside class="policy-sheet__framework" aria-label="Organizational review scope">
                  <h3>Review Scope</h3>
                  <ol>
                    <li><strong>Structure</strong> Organizational structure and responsibilities.</li>
                    <li><strong>Processes</strong> Management and administrative processes.</li>
                    <li><strong>Technology</strong> Tools and systems that support service delivery.</li>
                    <li><strong>Service Models</strong> Opportunities for shared or alternative delivery models.</li>
                    <li><strong>Alignment</strong> Whether municipal resources are aligned with Council&rsquo;s priorities.</li>
                  </ol>
                </aside>
              </div>
            </section>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP10</span>
              <div class="policy-doc__banner-text">
                <h2>Infrastructure Before Crisis</h2>
                <p>Building and renewing deliberately &mdash; not responding to emergency after emergency</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="infrastructure-heading">
              <h2 id="infrastructure-heading" class="sr-only">Infrastructure Before Crisis</h2>
              <div class="policy-sheet__copy">
                <p>One of municipal government&rsquo;s most important responsibilities is also one of its least glamorous: infrastructure. Watermains, sewers, roads, bridges, treatment systems, sidewalks, stormwater systems and municipal buildings often receive attention only when something fails. By then, the solution is usually more expensive.</p>
                <p>My career has taught me to look ahead &mdash; understand infrastructure condition and capacity, anticipate future requirements, establish realistic capital programs and position projects for funding before they become emergencies.</p>
                <p>That means doing the studies. Completing the design work. Understanding approvals. Knowing the costs. Establishing priorities. And managing projects carefully once construction begins.</p>
              </div>

              <aside class="policy-sheet__principle">
                <p><strong>Guiding Principle:</strong> Good infrastructure planning is good financial planning. Collingwood should be building and renewing infrastructure deliberately &mdash; not responding to crisis after crisis.</p>
              </aside>
            </section>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP10</span>
              <div class="policy-doc__banner-text">
                <h2>From Ideas to Action</h2>
                <p>A practical plan connecting every policy position in this vision</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="ideas-action-heading">
              <h2 id="ideas-action-heading" class="sr-only">From Ideas to Action</h2>
              <div class="policy-sheet__copy">
                <p>My Vision for Collingwood policy positions have deliberately gone beyond identifying problems. They ask a more important question: what can we actually do about them?</p>
                <p>We have examined opportunities to strengthen municipal financial management and long-term infrastructure planning. We have developed concepts for transforming underutilized downtown municipal parking lots into substantially more public parking, workforce rental housing and commercial space through carefully structured public/private partnerships. We have considered housing, transportation, active transportation, accessibility, economic opportunity and the continued vitality of our downtown. We have examined how Collingwood can strengthen relationships with Simcoe County and neighbouring municipalities while protecting our community&rsquo;s independence and interests.</p>
                <p>These are not disconnected ideas. Together, they form a practical plan for leading Collingwood forward.</p>
              </div>

              <h3 class="policy-sheet__subhead">How Responsible Government Works</h3>
              <div class="policy-sheet__tests">
                <div>
                  <span class="policy-sheet__test-icon" aria-hidden="true">
                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z"/></svg>
                  </span>
                  <h4>Study</h4>
                  <p>Understand the problem, alternatives and evidence before deciding.</p>
                </div>
                <div>
                  <span class="policy-sheet__test-icon" aria-hidden="true">
                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M9 17.17 4.83 13l-1.42 1.41L9 20 21 8l-1.41-1.41z"/></svg>
                  </span>
                  <h4>Test</h4>
                  <p>Evaluate feasibility, costs, risks and funding pathways.</p>
                </div>
                <div>
                  <span class="policy-sheet__test-icon" aria-hidden="true">
                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>
                  </span>
                  <h4>Consult</h4>
                  <p>Engage residents, staff, partners and affected stakeholders.</p>
                </div>
                <div>
                  <span class="policy-sheet__test-icon" aria-hidden="true">
                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2 2 7l10 5 9-4.5V17h2V7L12 2zm-6 9.5V16l6 3 6-3v-4.5l-6 3-6-3z"/></svg>
                  </span>
                  <h4>Refine</h4>
                  <p>Adjust scope, design and partnerships based on what we learn.</p>
                </div>
                <div>
                  <span class="policy-sheet__test-icon" aria-hidden="true">
                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M11.8 10.9c-2.27-.59-3-1.2-3-2.15 0-1.09 1.01-1.85 2.7-1.85 1.78 0 2.44.85 2.5 2.1h2.21c-.07-1.72-1.12-3.3-3.21-3.81V3h-3v2.16c-1.94.42-3.5 1.68-3.5 3.61 0 2.31 1.91 3.46 4.7 4.13 2.5.6 3 1.48 3 2.41 0 .69-.49 1.79-2.7 1.79-2.06 0-2.87-.92-2.98-2.1h-2.2c.12 2.19 1.76 3.42 3.68 3.83V21h3v-2.15c1.95-.37 3.5-1.5 3.5-3.55 0-2.84-2.43-3.81-4.7-4.4z"/></svg>
                  </span>
                  <h4>Fund</h4>
                  <p>Secure municipal, provincial, federal and partnership funding.</p>
                </div>
                <div>
                  <span class="policy-sheet__test-icon" aria-hidden="true">
                    <svg viewBox="0 0 24 24" fill="currentColor"><path d="M5 13.18v4L12 21l7-3.82v-4L12 17l-7-3.82zM12 3 1 9l11 6 9-4.91V17h2V9L12 3z"/></svg>
                  </span>
                  <h4>Deliver</h4>
                  <p>Manage projects carefully and report progress publicly.</p>
                </div>
              </div>

              <div class="policy-sheet__duo">
                <article>
                  <h3>Connecting the Vision</h3>
                  <p>PP10 brings together the practical plans developed across this series &mdash; from <a class="policy-ref" href="vision-pp01.html">PP01</a> water services and <a class="policy-ref" href="vision-pp04.html">PP04</a> financial sustainability to <a class="policy-ref" href="vision-pp05.html">PP05</a> transportation, <a class="policy-ref" href="vision-pp06.html">PP06</a> County relationships, <a class="policy-ref" href="vision-pp07.html">PP07</a> housing and <a class="policy-ref" href="vision-pp08.html">PP08</a> economic opportunity.</p>
                </article>
                <article>
                  <h3>Some Move Quickly, Some Require Study</h3>
                  <p>Some ideas can be implemented quickly. Others require further study, consultation, engineering, financial analysis or partnerships before Council should make a decision. That is how responsible municipal government should work.</p>
                </article>
              </div>
            </section>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP10</span>
              <div class="policy-doc__banner-text">
                <h2>The First 100 Days</h2>
                <p>Leadership must translate into action</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="first-100-heading">
              <h2 id="first-100-heading" class="sr-only">The First 100 Days</h2>
              <div class="policy-sheet__plan">
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">01</span>
                  <h3>Establish Council Priorities</h3>
                  <p>Bring Council together early to establish a manageable set of priorities for the four-year term and a clear plan for delivering them.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">02</span>
                  <h3>Organizational Review</h3>
                  <p>Initiate a comprehensive review of the Town&rsquo;s strengths, weaknesses, structure, processes and service-delivery models.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">03</span>
                  <h3>Strengthen Financial Management</h3>
                  <p>Begin preparation for a more rigorous budget process, including the gradual introduction of zero-based budgeting principles.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">04</span>
                  <h3>Review Major Capital Projects</h3>
                  <p>Confirm scope, costs, schedules, funding sources and risks for major municipal projects.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">05</span>
                  <h3>Strengthen Infrastructure Planning</h3>
                  <p>Identify priority infrastructure projects and determine which should be advanced for provincial and federal funding opportunities.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">06</span>
                  <h3>Advance Housing &amp; Downtown</h3>
                  <p>Ask staff and qualified consultants to further evaluate workforce housing, additional public parking and commercial development on underutilized municipal properties.</p>
                </article>
                <article>
                  <span class="policy-sheet__plan-num" aria-hidden="true">07</span>
                  <h3>Strengthen Government Relationships</h3>
                  <p>Meet with Simcoe County, neighbouring municipalities and provincial and federal representatives to identify shared priorities, partnerships and funding opportunities.</p>
                </article>
              </div>
            </section>

            <header class="policy-doc__banner">
              <span class="policy-doc__code">PP10</span>
              <div class="policy-doc__banner-text">
                <h2>Leading Collingwood Forward</h2>
                <p>Experience, fiscal responsibility, collaboration and results</p>
              </div>
            </header>

            <section class="policy-sheet" aria-labelledby="closing-heading">
              <h2 id="closing-heading" class="sr-only">Leading Collingwood Forward</h2>
              <div class="policy-sheet__duo">
                <article>
                  <h3>Why I Am Running</h3>
                  <p>I am not running for Mayor because I believe one person has all the answers. I am running because I know how to bring people together to find them &mdash; and how to turn good ideas into results.</p>
                  <p>I understand municipalities. I understand infrastructure. I understand project delivery and the importance of long-term financial planning. I know how projects move from an idea through study, design, funding and approvals and ultimately into construction. And I understand that every dollar Council spends belongs to the people we serve.</p>
                </article>
                <article>
                  <h3>What Collingwood Deserves</h3>
                  <ul>
                    <li>Investments supported by sound financial planning</li>
                    <li>Decisions based on evidence</li>
                    <li>A Council that works collaboratively</li>
                    <li>Residents who remain part of the conversation</li>
                    <li>Commitments Council is prepared to deliver</li>
                  </ul>
                </article>
              </div>

              <div class="policy-sheet__duo">
                <article>
                  <h3>Closing Message</h3>
                  <p>Collingwood should be ambitious about its future. But ambition must be matched by discipline. Our investments must be supported by sound financial planning. Our decisions must be based on evidence. Our Council must work collaboratively. Our residents must remain part of the conversation. And when Council makes a commitment, we must be prepared to deliver it.</p>
                  <p>Experience matters. Fiscal responsibility matters. Collaboration matters. Results matter. Together, we can lead Collingwood forward.</p>
                  <p class="policy-sheet__sign">&mdash; Norm</p>
                </article>
                <article>
                  <h3>Continuing the Conversation</h3>
                  <p>Vision for Collingwood is intended to start conversations &mdash; not end them. Constructive comments, additional ideas and alternative perspectives are welcome as this vision continues to be refined.</p>
                </article>
              </div>
            </section>

          </div>
        </div>

        <nav class="policy-pager policy-pager--footer" aria-label="Policy papers">
          <div class="container policy-pager__inner">
            <a class="policy-pager__link policy-pager__link--prev" href="vision-pp08.html">
              <span class="policy-pager__dir">Previous</span>
              <span class="policy-pager__label">PP08 Growing Opportunity</span>
            </a>
            <a class="policy-pager__all" href="vision-for-collingwood.html">ALL PAPERS</a>
            <span class="policy-pager__link policy-pager__link--placeholder" aria-hidden="true"></span>
          </div>
        </nav>
      </main>

'''

(ROOT / "vision-pp10.html").write_text(head + main + footer, encoding="utf-8")
print("Wrote vision-pp10.html")
