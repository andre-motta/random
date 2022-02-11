<head>
<meta http-equiv="content-type" content="text/html;charset=utf-8">
<title>wordle_solver.py</title>
<link rel="stylesheet" href="pycco.css">
<style type="text/css">
/*--------------------- Layout and Typography ----------------------------*/
body {
font-family: 'Palatino Linotype', 'Book Antiqua', Palatino, FreeSerif, serif;
font-size: 16px;
line-height: 24px;
color: #252519;
margin: 0; padding: 0;
background: #f5f5ff;
}
a {
color: #261a3b;
}
a:visited {
color: #261a3b;
}
p {
margin: 0 0 15px 0;
}
h1, h2, h3, h4, h5, h6 {
margin: 40px 0 15px 0;
}
h2, h3, h4, h5, h6 {
margin-top: 0;
}
#container {
background: white;
}
#container, div.section {
position: relative;
}
#background {
position: absolute;
top: 0; left: 580px; right: 0; bottom: 0;
background: #f5f5ff;
border-left: 1px solid #e5e5ee;
z-index: 0;
}
#jump_to, #jump_page {
background: white;
-webkit-box-shadow: 0 0 25px #777; -moz-box-shadow: 0 0 25px #777;
-webkit-border-bottom-left-radius: 5px; -moz-border-radius-bottomleft: 5px;
font: 10px Arial;
text-transform: uppercase;
cursor: pointer;
text-align: right;
}
#jump_to, #jump_wrapper {
position: fixed;
right: 0; top: 0;
padding: 5px 10px;
}
#jump_wrapper {
padding: 0;
display: none;
}
#jump_to:hover #jump_wrapper {
display: block;
}
#jump_page {
padding: 5px 0 3px;
margin: 0 0 25px 25px;
}
#jump_page .source {
display: block;
padding: 5px 10px;
text-decoration: none;
border-top: 1px solid #eee;
}
#jump_page .source:hover {
background: #f5f5ff;
}
#jump_page .source:first-child {
}
div.docs {
float: left;
max-width: 500px;
min-width: 500px;
min-height: 5px;
padding: 10px 25px 1px 50px;
vertical-align: top;
text-align: left;
}
.docs pre {
margin: 15px 0 15px;
padding-left: 15px;
}
.docs p tt, .docs p code {
background: #f8f8ff;
border: 1px solid #dedede;
font-size: 12px;
padding: 0 0.2em;
}
.octowrap {
position: relative;
}
.octothorpe {
font: 12px Arial;
text-decoration: none;
color: #454545;
position: absolute;
top: 3px; left: -20px;
padding: 1px 2px;
opacity: 0;
-webkit-transition: opacity 0.2s linear;
}
div.docs:hover .octothorpe {
opacity: 1;
}
div.code {
margin-left: 580px;
padding: 14px 15px 16px 50px;
vertical-align: top;
}
.code pre, .docs p code {
font-size: 12px;
}
pre, tt, code {
line-height: 18px;
font-family: Monaco, Consolas, "Lucida Console", monospace;
margin: 0; padding: 0;
}
div.clearall {
clear: both;
}


/*---------------------- Syntax Highlighting -----------------------------*/
td.linenos { background-color: #f0f0f0; padding-right: 10px; }
span.lineno { background-color: #f0f0f0; padding: 0 5px 0 5px; }
body .hll { background-color: #ffffcc }
body .c { color: #408080; font-style: italic }  /* Comment */
body .err { border: 1px solid #FF0000 } /* Error */
body .k { color: #954121 }  /* Keyword */
body .o { color: #666666 }  /* Operator */
body .cm { color: #408080; font-style: italic } /* Comment.Multiline */
body .cp { color: #BC7A00 } /* Comment.Preproc */
body .c1 { color: #408080; font-style: italic } /* Comment.Single */
body .cs { color: #408080; font-style: italic } /* Comment.Special */
body .gd { color: #A00000 } /* Generic.Deleted */
body .ge { font-style: italic } /* Generic.Emph */
body .gr { color: #FF0000 } /* Generic.Error */
body .gh { color: #000080; font-weight: bold }  /* Generic.Heading */
body .gi { color: #00A000 } /* Generic.Inserted */
body .go { color: #808080 } /* Generic.Output */
body .gp { color: #000080; font-weight: bold }  /* Generic.Prompt */
body .gs { font-weight: bold }  /* Generic.Strong */
body .gu { color: #800080; font-weight: bold }  /* Generic.Subheading */
body .gt { color: #0040D0 } /* Generic.Traceback */
body .kc { color: #954121 } /* Keyword.Constant */
body .kd { color: #954121; font-weight: bold }  /* Keyword.Declaration */
body .kn { color: #954121; font-weight: bold }  /* Keyword.Namespace */
body .kp { color: #954121 } /* Keyword.Pseudo */
body .kr { color: #954121; font-weight: bold }  /* Keyword.Reserved */
body .kt { color: #B00040 } /* Keyword.Type */
body .m { color: #666666 }  /* Literal.Number */
body .s { color: #219161 }  /* Literal.String */
body .na { color: #7D9029 } /* Name.Attribute */
body .nb { color: #954121 } /* Name.Builtin */
body .nc { color: #0000FF; font-weight: bold }  /* Name.Class */
body .no { color: #880000 } /* Name.Constant */
body .nd { color: #AA22FF } /* Name.Decorator */
body .ni { color: #999999; font-weight: bold }  /* Name.Entity */
body .ne { color: #D2413A; font-weight: bold }  /* Name.Exception */
body .nf { color: #0000FF } /* Name.Function */
body .nl { color: #A0A000 } /* Name.Label */
body .nn { color: #0000FF; font-weight: bold }  /* Name.Namespace */
body .nt { color: #954121; font-weight: bold }  /* Name.Tag */
body .nv { color: #19469D } /* Name.Variable */
body .ow { color: #AA22FF; font-weight: bold }  /* Operator.Word */
body .w { color: #bbbbbb }  /* Text.Whitespace */
body .mf { color: #666666 } /* Literal.Number.Float */
body .mh { color: #666666 } /* Literal.Number.Hex */
body .mi { color: #666666 } /* Literal.Number.Integer */
body .mo { color: #666666 } /* Literal.Number.Oct */
body .sb { color: #219161 } /* Literal.String.Backtick */
body .sc { color: #219161 } /* Literal.String.Char */
body .sd { color: #219161; font-style: italic } /* Literal.String.Doc */
body .s2 { color: #219161 } /* Literal.String.Double */
body .se { color: #BB6622; font-weight: bold }  /* Literal.String.Escape */
body .sh { color: #219161 } /* Literal.String.Heredoc */
body .si { color: #BB6688; font-weight: bold }  /* Literal.String.Interpol */
body .sx { color: #954121 } /* Literal.String.Other */
body .sr { color: #BB6688 } /* Literal.String.Regex */
body .s1 { color: #219161 } /* Literal.String.Single */
body .ss { color: #19469D } /* Literal.String.Symbol */
body .bp { color: #954121 } /* Name.Builtin.Pseudo */
body .vc { color: #19469D } /* Name.Variable.Class */
body .vg { color: #19469D } /* Name.Variable.Global */
body .vi { color: #19469D } /* Name.Variable.Instance */
body .il { color: #666666 } /* Literal.Number.Integer.Long */

</style>
</head>
<body>
<div id='container'>
<div id="background"></div>
<div class='section'>
<div class='docs'><h1>wordle_solver.py</h1></div>
</div>
<div class='clearall'>
<div class='section' id='section-0'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-0'>#</a>
</div>
<p>Copyright © 2021 by Andre Lustosa. All rights reserved.
Licensed under the Creative Commons Attribution 4.0 International License.
See LICENSE in the project root for license information.
Wordle Solver</p>
</div>
<div class='code'>
<div class="highlight"><pre><span></span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-1'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-1'>#</a>
</div>
<p>This script allows you to solve wordle puzzles.</p>
<p>Usage:  python wordle_solver.py  <words_file></p>
<p>This script requires a dataset of all words acceptable by wordle</p>
<p>This file cannot be imported, it must be run as a script.</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="kn">import</span> <span class="nn">operator</span>
<span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">sys</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-2'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-2'>#</a>
</div>
<p>Main</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">def</span> <span class="nf">main</span><span class="p">():</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-3'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-3'>#</a>
</div>
<p>Parameters:
None
Returns:
None</p>
<p>Initialize state variables</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="n">contained_letters</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">excluded_letters</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">position_letters</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">notposition_letters</span> <span class="o">=</span> <span class="p">[]</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-4'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-4'>#</a>
</div>
<p>Check for correct number of arguments</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">)</span> <span class="o">&lt;</span> <span class="mi">2</span><span class="p">:</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Usage:  python wordle_solver.py &lt;words_file&gt;&quot;</span><span class="p">)</span>
<span class="n">sys</span><span class="o">.</span><span class="n">exit</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-5'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-5'>#</a>
</div>
<p>Get the words file</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="n">dictionary_file</span> <span class="o">=</span> <span class="n">sys</span><span class="o">.</span><span class="n">argv</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;STARTING GUESS = ALERT&quot;</span><span class="p">)</span>

<span class="k">with</span> <span class="nb">open</span><span class="p">(</span><span class="n">dictionary_file</span><span class="p">,</span><span class="s1">&#39;r&#39;</span><span class="p">)</span> <span class="k">as</span> <span class="n">file</span><span class="p">:</span>
<span class="n">words</span> <span class="o">=</span> <span class="n">file</span><span class="o">.</span><span class="n">readlines</span><span class="p">()</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-6'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-6'>#</a>
</div>
<p>Print the avaiable commands</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Available commands:&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">a &lt;letter&gt; &lt;position&gt; - informs a letter is part of the word and is in the correct position&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">a &lt;letter&gt; n &lt;position&gt; - informs a letter is part of the word and is NOT in the correct position&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">r &lt;letter&gt; - informs a letter is not part of the word&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">u &lt;a/r&gt; &lt;letter&gt; - undoes the informed command. Positional variables are also undone&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">p - processes the current state of the puzzle and prints the current suggestions&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">c - clears the console window&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">? - prints this list of commands&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">x - resets the program to its initial state&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">q - quits the program&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">Spaces are ignored in the commands, feel free to not use them once you are familiar with them</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span>

<span class="n">clear</span> <span class="o">=</span> <span class="k">lambda</span><span class="p">:</span> <span class="n">os</span><span class="o">.</span><span class="n">system</span><span class="p">(</span><span class="s1">&#39;cls&#39;</span> <span class="k">if</span> <span class="n">os</span><span class="o">.</span><span class="n">name</span> <span class="ow">in</span> <span class="p">(</span><span class="s1">&#39;nt&#39;</span><span class="p">,</span> <span class="s1">&#39;dos&#39;</span><span class="p">)</span> <span class="k">else</span> <span class="s1">&#39;clear&#39;</span><span class="p">)</span>


<span class="k">while</span><span class="p">(</span><span class="mi">1</span><span class="p">):</span>
<span class="n">command</span> <span class="o">=</span> <span class="s2">&quot;&quot;</span><span class="o">.</span><span class="n">join</span><span class="p">(</span><span class="nb">input</span><span class="p">(</span><span class="s2">&quot;Enter a command: &quot;</span><span class="p">)</span><span class="o">.</span><span class="n">split</span><span class="p">())</span>
<span class="k">if</span> <span class="n">command</span> <span class="o">==</span> <span class="s2">&quot;&quot;</span> <span class="ow">or</span> <span class="n">command</span> <span class="o">==</span> <span class="s2">&quot; &quot;</span> <span class="ow">or</span> <span class="n">command</span> <span class="o">==</span> <span class="kc">None</span><span class="p">:</span>
<span class="k">continue</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-7'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-7'>#</a>
</div>
<p>Help command</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">elif</span> <span class="n">command</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;?&quot;</span><span class="p">:</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Available commands:&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">a &lt;letter&gt; &lt;position&gt; - informs a letter is part of the word and is in the correct position&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">a &lt;letter&gt; n &lt;position&gt; - informs a letter is part of the word and is NOT in the correct position&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">r &lt;letter&gt; - informs a letter is not part of the word&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">u &lt;a/r&gt; &lt;letter&gt; - undoes the informed command. Positional variables are also undone&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">p - processes the current state of the puzzle and prints the current suggestions&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">c - clears the console window&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">? - prints this list of commands&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">x - resets the program to its initial state&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\t</span><span class="s2">q - quits the program&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">Spaces are ignored in the commands, feel free to not use them once you are familiar with them</span><span class="se">\n</span><span class="s2">&quot;</span><span class="p">)</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-8'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-8'>#</a>
</div>
<p>Restart command</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">elif</span> <span class="n">command</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;x&quot;</span><span class="p">:</span>
<span class="n">contained_letters</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">excluded_letters</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">position_letters</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">notposition_letters</span> <span class="o">=</span> <span class="p">[]</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;STARTING GUESS = ALERT&quot;</span><span class="p">)</span>
<span class="k">continue</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-9'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-9'>#</a>
</div>
<p>Clear command</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">elif</span> <span class="n">command</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;c&quot;</span><span class="p">:</span>
<span class="n">clear</span><span class="p">()</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-10'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-10'>#</a>
</div>
<p>Quit command</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">elif</span> <span class="n">command</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;q&quot;</span><span class="p">:</span>
<span class="k">break</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-11'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-11'>#</a>
</div>
<p>Add letter command</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">elif</span> <span class="n">command</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;a&quot;</span><span class="p">:</span>
<span class="n">letter</span> <span class="o">=</span> <span class="n">command</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>

<span class="k">if</span> <span class="n">letter</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">contained_letters</span><span class="p">:</span>
<span class="n">contained_letters</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">letter</span><span class="p">)</span>

<span class="k">if</span> <span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">command</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">2</span> <span class="p">):</span>
<span class="k">if</span> <span class="n">command</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;n&quot;</span><span class="p">:</span>
<span class="n">position</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">command</span><span class="p">[</span><span class="mi">3</span><span class="p">])</span> <span class="o">-</span> <span class="mi">1</span>
<span class="k">if</span> <span class="p">(</span><span class="n">letter</span><span class="p">,</span> <span class="n">position</span><span class="p">)</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">notposition_letters</span><span class="p">:</span>
<span class="n">notposition_letters</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">letter</span><span class="p">,</span><span class="n">position</span><span class="p">))</span>
<span class="k">else</span><span class="p">:</span>
<span class="n">position</span> <span class="o">=</span> <span class="nb">int</span><span class="p">(</span><span class="n">command</span><span class="p">[</span><span class="mi">2</span><span class="p">])</span> <span class="o">-</span> <span class="mi">1</span>
<span class="k">if</span> <span class="p">(</span><span class="n">letter</span><span class="p">,</span> <span class="n">position</span><span class="p">)</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">position_letters</span><span class="p">:</span>
<span class="n">position_letters</span><span class="o">.</span><span class="n">append</span><span class="p">((</span><span class="n">letter</span><span class="p">,</span><span class="n">position</span><span class="p">))</span>
<span class="k">continue</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-12'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-12'>#</a>
</div>
<p>Remove letter command</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">elif</span> <span class="n">command</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;r&quot;</span><span class="p">:</span>
<span class="n">letter</span> <span class="o">=</span> <span class="n">command</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
<span class="k">if</span> <span class="n">letter</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">excluded_letters</span><span class="p">:</span>
<span class="n">excluded_letters</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">letter</span><span class="p">)</span>
<span class="k">continue</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-13'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-13'>#</a>
</div>
<p>Undo operation command</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">elif</span> <span class="n">command</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;u&quot;</span><span class="p">:</span>
<span class="k">if</span> <span class="n">command</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;a&quot;</span><span class="p">:</span>
<span class="n">letter</span> <span class="o">=</span> <span class="n">command</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
<span class="n">contained_letters</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">contained_letters</span> <span class="k">if</span> <span class="n">x</span> <span class="o">!=</span> <span class="n">letter</span><span class="p">]</span>

<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">position_letters</span><span class="p">)):</span>
<span class="k">if</span> <span class="n">position_letters</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="n">letter</span><span class="p">:</span>
<span class="n">position_letters</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">position_letters</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
<span class="k">break</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">notposition_letters</span><span class="p">)):</span>
<span class="k">if</span> <span class="n">notposition_letters</span><span class="p">[</span><span class="n">i</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span> <span class="o">==</span> <span class="n">letter</span><span class="p">:</span>
<span class="n">notposition_letters</span><span class="o">.</span><span class="n">remove</span><span class="p">(</span><span class="n">notposition_letters</span><span class="p">[</span><span class="n">i</span><span class="p">])</span>
<span class="k">break</span>
<span class="k">continue</span>

<span class="k">if</span> <span class="n">command</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="s2">&quot;r&quot;</span><span class="p">:</span>
<span class="n">letter</span> <span class="o">=</span> <span class="n">command</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span>
<span class="n">excluded_letters</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">excluded_letters</span> <span class="k">if</span> <span class="n">x</span> <span class="o">!=</span> <span class="n">letter</span><span class="p">]</span>
<span class="k">continue</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-14'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-14'>#</a>
</div>
<p>Process state and print command</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">elif</span> <span class="n">command</span> <span class="o">==</span> <span class="s2">&quot;p&quot;</span><span class="p">:</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-15'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-15'>#</a>
</div>
<p>Get the words that match the current state</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="n">filtered_words</span> <span class="o">=</span> <span class="p">[</span><span class="n">word</span> <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">words</span> <span class="k">if</span> <span class="nb">all</span><span class="p">([</span><span class="n">letter</span> <span class="ow">in</span> <span class="n">word</span> <span class="k">for</span> <span class="n">letter</span> <span class="ow">in</span> <span class="n">contained_letters</span><span class="p">])]</span>
<span class="n">filtered_words</span> <span class="o">=</span> <span class="p">[</span><span class="n">word</span> <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">filtered_words</span> <span class="k">if</span> <span class="ow">not</span> <span class="nb">any</span><span class="p">([</span><span class="n">letter</span> <span class="ow">in</span> <span class="n">word</span> <span class="k">for</span> <span class="n">letter</span> <span class="ow">in</span> <span class="n">excluded_letters</span><span class="p">])]</span>
<span class="k">for</span> <span class="n">letter</span><span class="p">,</span> <span class="n">position</span> <span class="ow">in</span> <span class="n">position_letters</span><span class="p">:</span>
<span class="n">filtered_words</span> <span class="o">=</span> <span class="p">[</span><span class="n">word</span> <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">filtered_words</span> <span class="k">if</span> <span class="n">word</span><span class="p">[</span><span class="n">position</span><span class="p">]</span> <span class="o">==</span> <span class="n">letter</span><span class="p">]</span>
<span class="k">for</span> <span class="n">letter</span><span class="p">,</span> <span class="n">position</span> <span class="ow">in</span> <span class="n">notposition_letters</span><span class="p">:</span>
<span class="n">filtered_words</span> <span class="o">=</span> <span class="p">[</span><span class="n">word</span> <span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">filtered_words</span> <span class="k">if</span> <span class="n">word</span><span class="p">[</span><span class="n">position</span><span class="p">]</span> <span class="o">!=</span> <span class="n">letter</span><span class="p">]</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-16'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-16'>#</a>
</div>
<p>Print the current state</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Excluded:&quot;</span><span class="p">,</span> <span class="n">excluded_letters</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Contained:&quot;</span><span class="p">,</span> <span class="n">contained_letters</span><span class="p">)</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-17'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-17'>#</a>
</div>
<p>Print the current known letters</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;What we know:&quot;</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">5</span><span class="p">):</span>
<span class="k">if</span> <span class="n">i</span> <span class="ow">in</span> <span class="p">[</span><span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">position_letters</span><span class="p">]:</span>
<span class="nb">print</span><span class="p">(</span><span class="nb">next</span><span class="p">(</span><span class="n">x</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="n">position_letters</span> <span class="k">if</span> <span class="n">x</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">==</span> <span class="n">i</span><span class="p">),</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
<span class="k">else</span><span class="p">:</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;?&quot;</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot;&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-18'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-18'>#</a>
</div>
<p>Print the number of words that match the current state</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;There are&quot;</span><span class="p">,</span> <span class="nb">len</span><span class="p">(</span><span class="n">filtered_words</span><span class="p">),</span> <span class="s2">&quot;possible words&quot;</span><span class="p">)</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-19'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-19'>#</a>
</div>
<p>Calculate the frequency of each letter in the surviving words</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="n">entropy</span> <span class="o">=</span> <span class="p">{}</span>
<span class="n">letters</span> <span class="o">=</span> <span class="p">[</span><span class="n">x</span> <span class="k">for</span> <span class="n">x</span> <span class="ow">in</span> <span class="s2">&quot;abcdefghijklmnopqrstuvwxyz&quot;</span> <span class="k">if</span> <span class="n">x</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">excluded_letters</span> <span class="ow">and</span> <span class="n">x</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">contained_letters</span><span class="p">]</span>

<span class="k">for</span> <span class="n">letter</span> <span class="ow">in</span> <span class="n">letters</span><span class="p">:</span>
<span class="n">entropy</span><span class="p">[</span><span class="n">letter</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>

<span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">filtered_words</span><span class="p">:</span>
<span class="k">for</span> <span class="n">letter</span> <span class="ow">in</span> <span class="n">word</span><span class="p">:</span>
<span class="k">if</span> <span class="n">letter</span> <span class="ow">in</span> <span class="n">entropy</span><span class="p">:</span>
<span class="n">entropy</span><span class="p">[</span><span class="n">letter</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-20'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-20'>#</a>
</div>
<p>Print remaining letters in descending order of frequency</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Remaining letters:&quot;</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">letter</span> <span class="ow">in</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">entropy</span><span class="p">,</span> <span class="n">key</span><span class="o">=</span><span class="n">entropy</span><span class="o">.</span><span class="n">get</span><span class="p">,</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">):</span>
<span class="nb">print</span><span class="p">(</span><span class="n">letter</span><span class="p">,</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot;, &quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-21'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-21'>#</a>
</div>
<p>Using the frequency of each letter
Calculate an entropy score for each word that matches the current state
Normalize the entropy score by the number of words
Only take into account unique letters in the word</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="n">entropy_words</span> <span class="o">=</span> <span class="p">{}</span>
<span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">filtered_words</span><span class="p">:</span>
<span class="n">entropy_words</span><span class="p">[</span><span class="n">word</span><span class="p">]</span> <span class="o">=</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">filtered_words</span><span class="p">:</span>
<span class="n">seen</span> <span class="o">=</span> <span class="nb">set</span><span class="p">()</span>
<span class="k">for</span> <span class="n">letter</span> <span class="ow">in</span> <span class="n">word</span><span class="p">:</span>
<span class="k">if</span> <span class="n">letter</span> <span class="ow">in</span> <span class="n">entropy</span> <span class="ow">and</span> <span class="n">letter</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">seen</span><span class="p">:</span>
<span class="n">entropy_words</span><span class="p">[</span><span class="n">word</span><span class="p">]</span> <span class="o">+=</span> <span class="n">entropy</span><span class="p">[</span><span class="n">letter</span><span class="p">]</span>
<span class="n">seen</span><span class="o">.</span><span class="n">add</span><span class="p">(</span><span class="n">letter</span><span class="p">)</span>
<span class="k">for</span> <span class="n">word</span> <span class="ow">in</span> <span class="n">filtered_words</span><span class="p">:</span>
<span class="n">entropy_words</span><span class="p">[</span><span class="n">word</span><span class="p">]</span> <span class="o">=</span> <span class="n">entropy_words</span><span class="p">[</span><span class="n">word</span><span class="p">]</span> <span class="o">/</span> <span class="nb">len</span><span class="p">(</span><span class="n">filtered_words</span><span class="p">)</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-22'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-22'>#</a>
</div>
<p>Sort the words by their entropy score</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="n">sorted_words</span> <span class="o">=</span> <span class="nb">sorted</span><span class="p">(</span><span class="n">entropy_words</span><span class="o">.</span><span class="n">items</span><span class="p">(),</span> <span class="n">key</span><span class="o">=</span><span class="n">operator</span><span class="o">.</span><span class="n">itemgetter</span><span class="p">(</span><span class="mi">1</span><span class="p">),</span> <span class="n">reverse</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-23'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-23'>#</a>
</div>
<p>If there are no words that match the current state, the puzzle is solved
Print the solution and reset the program</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">if</span> <span class="nb">len</span><span class="p">(</span><span class="n">sorted_words</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;There is only one possible word you won!&quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;SOLUTION:&quot;</span><span class="p">,</span> <span class="n">sorted_words</span><span class="p">[</span><span class="mi">0</span><span class="p">][</span><span class="mi">0</span><span class="p">])</span>
<span class="n">contained_letters</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">excluded_letters</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">position_letters</span> <span class="o">=</span> <span class="p">[]</span>
<span class="n">notposition_letters</span> <span class="o">=</span> <span class="p">[]</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;STARTING GUESS = ALERT&quot;</span><span class="p">)</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-24'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-24'>#</a>
</div>
<p>If there are multiple words that match the current state
Print the suggestions in descending order of entropy score</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">else</span><span class="p">:</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-25'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-25'>#</a>
</div>
<p>Print the entropy scores in scientific notation</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Suggestions:&quot;</span><span class="p">)</span>
<span class="k">for</span> <span class="n">word</span><span class="p">,</span> <span class="n">entropy</span> <span class="ow">in</span> <span class="n">sorted_words</span><span class="p">:</span>
<span class="nb">print</span><span class="p">(</span><span class="n">word</span><span class="o">.</span><span class="n">strip</span><span class="p">(),</span> <span class="s2">&quot;:&quot;</span><span class="p">,</span> <span class="s2">&quot;</span><span class="si">{:.2e}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">entropy</span><span class="p">),</span> <span class="n">end</span><span class="o">=</span><span class="s2">&quot; &quot;</span><span class="p">)</span>
<span class="nb">print</span><span class="p">()</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-26'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-26'>#</a>
</div>
<p>Invalid command</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">else</span><span class="p">:</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Invalid command&quot;</span><span class="p">)</span>
<span class="k">continue</span></pre></div>
</div>
</div>
<div class='clearall'></div>
<div class='section' id='section-27'>
<div class='docs'>
<div class='octowrap'>
<a class='octothorpe' href='#section-27'>#</a>
</div>
<p>Run the program</p>
</div>
<div class='code'>
<div class="highlight"><pre><span class="k">if</span> <span class="vm">__name__</span> <span class="o">==</span> <span class="s2">&quot;__main__&quot;</span><span class="p">:</span>
<span class="n">main</span><span class="p">()</span>

</pre></div>
</div>
</div>
<div class='clearall'></div>
</div>
</body>
