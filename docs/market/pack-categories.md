# 包装对象分类

<div class="page-cats">
  <h2 style="margin:0 0 24px">What do you want to pack?</h2>
  <div class="cat-grid">
    <a class="cat" href="../customer-scenarios/">
      <div class="cat-icon">
        <svg viewBox="0 0 100 100" aria-label="Meat">
          <path d="M20 55c0-16 14-24 28-24 10 0 22 5 26 12 3 6 1 14-5 18-8 6-18 9-27 9-12 0-22-6-22-15z"/>
          <path d="M35 54c8-6 18-6 26 0"/>
        </svg>
      </div>
      <div class="cat-label">MEAT</div>
    </a>
    <a class="cat" href="../customer-scenarios/">
      <div class="cat-icon">
        <svg viewBox="0 0 100 100" aria-label="Poultry">
          <path d="M30 60c0-12 10-20 24-20 6 0 10 2 14 6l-6 6c2 4 2 8 0 12-4 6-12 8-20 8-8 0-12-4-12-12z"/>
          <circle cx="38" cy="56" r="2"/>
        </svg>
      </div>
      <div class="cat-label">POULTRY</div>
    </a>
    <a class="cat" href="../../technology/packaging-forms/">
      <div class="cat-icon">
        <svg viewBox="0 0 100 100" aria-label="Cheese">
          <path d="M30 70l40-16-14-18-40 16z"/>
          <circle cx="60" cy="53" r="4"/><circle cx="45" cy="60" r="3"/>
        </svg>
      </div>
      <div class="cat-label">CHEESE</div>
    </a>
    <a class="cat" href="../customer-scenarios/">
      <div class="cat-icon">
        <svg viewBox="0 0 100 100" aria-label="Produce">
          <path d="M50 30c-4 4-6 8-6 12 0 8 8 16 16 16 8 0 16-8 16-16 0-8-8-16-16-16-4 0-8 2-10 4"/>
          <path d="M50 30c0-6 4-10 10-12"/>
        </svg>
      </div>
      <div class="cat-label">PRODUCE</div>
    </a>
    <a class="cat" href="../ready-meals/">
      <div class="cat-icon">
        <svg viewBox="0 0 100 100" aria-label="Bakery">
          <path d="M30 65c0-10 8-15 20-15s20 5 20 15-8 15-20 15-20-5-20-15z"/>
          <path d="M40 50c0-6 6-10 10-10s10 4 10 10"/>
        </svg>
      </div>
      <div class="cat-label">BAKERY</div>
    </a>
    <a class="cat" href="../ready-meals/">
      <div class="cat-icon">
        <svg viewBox="0 0 100 100" aria-label="Ready Meals">
          <path d="M30 70l40-10-10-20-40 10z"/><circle cx="54" cy="54" r="3"/><circle cx="44" cy="57" r="3"/>
        </svg>
      </div>
      <div class="cat-label">READY MEALS</div>
    </a>
    <a class="cat" href="../customer-scenarios/">
      <div class="cat-icon">
        <svg viewBox="0 0 100 100" aria-label="Fish-Seafood">
          <path d="M28 60c10 10 24 10 34 0l-8-6 8-6c-10-10-24-10-34 0l-6 6z"/>
          <circle cx="38" cy="56" r="2"/>
        </svg>
      </div>
      <div class="cat-label">FISH-SEAFOOD</div>
    </a>
    <a class="cat" href="../../technology/packaging-forms/">
      <div class="cat-icon">
        <svg viewBox="0 0 100 100" aria-label="Medical-Pharma">
          <path d="M30 60l30-30 10 10-30 30-10-10z"/>
          <path d="M62 38l6-6"/>
        </svg>
      </div>
      <div class="cat-label">MEDICAL-PHARMA</div>
    </a>
  </div>
</div>

<style>
.page-cats{padding:40px;border-radius:12px}
.cat-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:36px}
.cat{display:flex;flex-direction:column;align-items:center;text-decoration:none;color:inherit}
.cat-icon{width:160px;height:160px;border-radius:50%;background:#e9edf3;display:flex;align-items:center;justify-content:center;transition:transform .2s ease, background .2s ease;color:#333}
.cat-label{margin-top:14px;font-size:14px;letter-spacing:.5px;text-transform:uppercase;color:inherit}
.cat:hover .cat-icon{transform:scale(1.04);background:#dfe4ea}
.cat svg{width:88px;height:88px;stroke:currentColor;fill:none;stroke-width:2}
@media (max-width:980px){.cat-grid{grid-template-columns:repeat(2,1fr)}.cat-icon{width:140px;height:140px}}
</style>