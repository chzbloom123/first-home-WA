HOME_INTRO = """
This page walks you through the whole process, from first thought to keys in hand. It takes about ten minutes to read. You do not need to click anything to follow it. The links are there if you want to do a step or check a fact.
"""

HOME_SHORT = """
- **You apply for every common loan through a lender.** FHA, VA and USDA do not hand out loans at a government counter.
- **You need three piles of cash:** a down payment, closing costs, and a cushion for moving and early repairs.
- **Washington gives you a short window to cancel** after you get the seller's disclosure form.
- **The inspection is your one close look** at the house before you are committed.
- **Many dollar amounts and deadlines are set in your contract, not in law.** Read every blank before you sign.
"""

HOME_TIME = """
No Washington agency publishes a typical timeline. Freddie Mac's national guide says buyers look at about 10 homes over about 10 weeks, and that closing comes 30 to 60 days after a seller accepts your offer. Getting your credit and savings ready comes before all of that and has no set length.
"""

STEPS = [
 dict(id="step-1", title="Get your money ready",
  who="You", money="Nothing yet", time="As long as you need",
  body="""
Start with your credit. You can pull free reports from all three credit bureaus every week at [AnnualCreditReport.com](https://www.annualcreditreport.com). Fixing a mistake is free, and the bureau has 30 days to look into it.

Next, size up the cash. You need three piles:

- **A down payment.** Zero on VA and USDA loans if you qualify. As low as 3% on some conventional loans. At least 3.5% on an FHA loan.
- **Closing costs.** The federal consumer agency says these run about 2% to 5% of the price, on top of the down payment.
- **A cushion.** Moving, utility set-up and early repairs all cost money. No official number exists for this one.

Lenders also look at your debt-to-income ratio. That is your monthly debt payments, with the new house payment added in, divided by your income before taxes. Each loan program sets its own ceiling.

One warning from the federal consumer agency: do not open new credit just before or during the loan process.
""",
  deeper=("money", "Money and costs"), links=[]),

 dict(id="step-2", title="Take the free homebuyer class",
  who="Loan officers and real estate professionals who partner with the state Housing Finance Commission", money="Free, or $50 for the self-study version", time="About five hours",
  body="""
Washington's Housing Finance Commission sponsors a free homebuyer class. It runs in person and by live video almost every day.

You **must** take it if you want a Commission home loan or the state's down payment help. Each person who signs the loan needs their own certificate, and the certificate lasts two years. If you are not using those programs the class is optional, but it covers this whole process with a live teacher you can ask questions.

The state's down payment help is a second loan with no monthly payments. You pay it back when you sell, refinance or move out. Tri-Cities buyers may also have a local program.
""",
  deeper=("help", "Help and classes"),
  links=[("Find a class", "https://heretohome.org/homebuyer-education-classes-list/")]),

 dict(id="step-3", title="Talk to lenders and get preapproved",
  who="A loan officer at a bank, credit union or mortgage company", money="Only a credit report fee at this stage", time="Varies by lender",
  body="""
Here is the idea most first-time buyers miss. **FHA insures loans. VA and USDA guarantee loans. A lender makes the loan.** So you apply through a lender for all of them, and the steps are the same.

Ask for a prequalification or preapproval letter. Lenders use those two words differently, and neither one is a promised loan.

Then ask for a **Loan Estimate**. It is a three-page form that shows the rate, the monthly payment and the closing costs. A lender must send it within three business days once it has six things: your name, income, Social Security number, the property address, the home's estimated value and the loan amount you want.

Get Loan Estimates from more than one lender and compare them. Mortgage credit checks inside a 45-day window count as one, so shopping around does little harm to your score. Until you have a Loan Estimate and say "go ahead," a lender may charge you only for the credit report.
""",
  deeper=("loans", "Loan types"),
  links=[("Check a loan officer's license", "https://www.nmlsconsumeraccess.org/"),
         ("How to compare Loan Estimates", "https://www.consumerfinance.gov/owning-a-home/compare/")]),

 dict(id="step-4", title="Hire a broker and look at homes",
  who="A real estate broker, which is Washington's word for agent", money="Nothing yet", time="About 10 weeks for a typical buyer",
  body="""
In Washington a real estate firm must have a written **brokerage services agreement** with you. It lasts 60 days unless you agree to longer. It names your broker, says whether the deal is exclusive, and states what the firm will be paid.

That pay can come from you, the seller, or be shared between firms. It is whatever the agreement says, so read that part before you sign. Your broker must also hand you a state pamphlet called "Real Estate Brokerage in Washington."

The kind of home you pick changes the process. A condo, a manufactured home, a brand-new house and a duplex each add their own rules.

In the Tri-Cities, ask one extra question about every house: which irrigation district is it in? The yearly charge stays with the land whether or not you use the water.
""",
  deeper=("home-types", "Home types"),
  links=[("Check a broker's license", "https://professions.dol.wa.gov/s/license-lookup")]),

 dict(id="step-5", title="Make an offer and put down earnest money",
  who="You, your broker and the seller", money="Earnest money, held by a neutral party", time="A day or two to reach a deal",
  body="""
Your offer is a contract. When you and the seller have both signed, that is called **mutual acceptance**, and the clocks start.

The contract is a standard form with blanks, plus add-on pages called **contingencies**. A contingency is a condition that lets you back out if something goes wrong. Common ones cover your loan, the inspection and the title.

**The deadlines for each one are written into your contract.** State law does not set them. Ask your broker to walk you through every blank and every date.

**Earnest money** is a deposit that shows you are serious. No law sets the amount. It goes to a neutral holder and counts toward the price at closing. If you back out for a reason your contract does not allow, you can lose it.
""",
  deeper=("contract", "Contract and closing"), links=[]),

 dict(id="step-6", title="Read the disclosure and inspect the house",
  who="The seller, and a home inspector you hire", money="The inspection fee, paid by you", time="2 to 3 hours on site, plus time for the report",
  body="""
Two things happen fast after mutual acceptance.

**The seller's disclosure form.** The seller must give you a filled-in form about the home's condition within five business days, unless you both agree to a different date. You then have **three business days** to accept it or cancel in writing and get your deposit back. If you say nothing, that counts as accepting it. The form is not a warranty.

**Your inspection.** Washington licenses home inspectors. An inspection is a visual check of what the inspector can safely reach. It does **not** cover the sewer line, a septic system, a well, radon or mold unless you add those. Only an inspector with a second state license can name a wood-eating insect.

An appraisal is not an inspection. The appraiser works out value for the lender. The inspector checks condition for you.

If your contract has an inspection contingency, you have three choices inside its deadline. You can ask the seller to fix things or give a credit. You can accept the house as it is. Or you can cancel.
""",
  deeper=("inspection", "Inspections"),
  links=[("Check an inspector's license", "https://professions.dol.wa.gov/s/license-lookup")]),

 dict(id="step-7", title="Finish the loan: appraisal, title and insurance",
  who="Your lender, an appraiser, a title company and an insurance agent", money="The appraisal fee, then your first insurance premium", time="Most of the 30 to 60 days before closing",
  body="""
Tell one lender to go ahead, and lock your rate. Rate locks usually last 30, 45 or 60 days.

The lender orders an **appraisal**. You have a right to a free copy no later than three days before closing.

**Underwriting** is the lender checking your file and the home. Do not take on new debt during this stretch. The federal consumer agency warns that even financing a refrigerator can make the loan harder to get.

The **title company** searches the home's ownership records and sends a preliminary commitment. Read its list of exceptions, because those are the things the policy will not cover. The lender's title policy protects only the lender. The owner's policy protects you and is optional. Washington's insurance regulator says most sellers pay for the owner's policy, and that you have the final say on which title company is used.

Your lender will also require **homeowners insurance** before closing. Get more than one quote. A standard policy does not cover floods or earthquakes.
""",
  deeper=("first-year", "Insurance and your first year"), links=[]),

 dict(id="step-8", title="Close and get your keys",
  who="An escrow agent or closing officer", money="Your down payment and closing costs", time="Signing, then recording, usually within days",
  body="""
You must get a **Closing Disclosure** at least three business days before you sign. It shows the final numbers. Lay it next to your Loan Estimate and ask about anything that changed.

**Watch for wire fraud.** Criminals send fake emails with "new wiring instructions" just before closing. Before you send money, call your closer at a phone number you already know. Never use a number, link or attachment from the email.

Do a final walk-through of the house before you sign. Check that agreed repairs were made and that promised items are still there.

In Washington an escrow agent or a title company usually runs the closing. No source we found requires a lawyer, and you may hire one if you want one.

Signing day is usually not the day you own the home. After you sign, the lender sends the money and the deed is recorded at the county. Then the sale is closed. Your contract sets the day you get the keys.
""",
  deeper=("first-year", "Your first year"),
  links=[("Closing checklist from the federal consumer agency", "https://files.consumerfinance.gov/f/documents/cfpb_buying-a-house_mortgage-closing_checklist.pdf"),
         ("How closing scams work", "https://www.consumerfinance.gov/owning-a-home/beware-mortgage-closing-scams/")]),
]

HOME_OUTRO = """
That is the whole path. The sections in the menu go deeper on each part, and the checklist puts every step on one page you can tick off.
"""
