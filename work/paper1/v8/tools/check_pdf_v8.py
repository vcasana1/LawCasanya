#!/usr/bin/env python3
"""Structural verification; visual inspection must also be performed."""
from pathlib import Path
import json
import re
import hashlib
from collections import Counter
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
PDF=ROOT/'manuscript/prime_corrected_clock_v8.pdf'
reader=PdfReader(PDF)
destinations=reader.named_destinations
types=Counter()
tooltips=[]
missing=[]
external=[]
for page in reader.pages:
    for ref in page.get('/Annots',[]):
        a=ref.get_object()
        types[str(a.get('/Subtype',''))]+=1
        if '/TU' in a:
            tooltips.append(str(a['/TU']))
        action=a.get('/A',{})
        if hasattr(action,'get_object'): action=action.get_object()
        if action.get('/S')=='/GoTo':
            target=action.get('/D')
            if isinstance(target,str) and target not in destinations:
                missing.append(target)
        if action.get('/S')=='/URI':external.append(str(action.get('/URI','')))
text='\n'.join(page.extract_text() for page in reader.pages)
tex=(ROOT/'manuscript/prime_corrected_clock_v8.tex').read_text()
assert not missing,missing
assert tooltips and not any(t.startswith('Reference: ') for t in tooltips)
assert 'Established antecedent' in text and 'Present result and scope' in text
assert not re.search(r'\b(?:Theorem F|Theorem 10.*sublevel)\b',text)
assert (ROOT/'manuscript/prime_corrected_clock_v8.tex').read_bytes()==(ROOT/'manuscript/prime_corrected_clock_v8.txt').read_bytes()
assert '??' not in text
labels=re.findall(r'\\label\{([^}]+)\}',tex)
assert len(labels)==len(set(labels))
refs=re.findall(r'\\(?:CGref|CGeqref)\{([^}]+)\}',tex)
assert set(refs)<=set(labels)
results={
 'pages':len(reader.pages),'annotation_types':dict(types),
 'tooltip_widgets':len(tooltips),'tooltip_examples':tooltips[:4],
 'named_destinations':len(destinations),'missing_internal_destinations':missing,
 'external_links':len(external),'comparison_table_present':True,
 'removed_project_name_absent':True,'no_unresolved_question_marks':True,
 'unique_labels':len(labels),'tex_txt_identical':True,
 'no_new_sublevel_theorem':True,
 'pdf_sha256':hashlib.sha256(PDF.read_bytes()).hexdigest(),
 'visual_review':'Performed separately on page renderings; not inferred from structural assertions.',
 'viewer_limit':'Annotation tooltips require support in the reader application.'
}
(ROOT/'audit/pdf_checks.json').write_text(json.dumps(results,indent=2,ensure_ascii=False)+'\n')
print(json.dumps(results,indent=2,ensure_ascii=False))
