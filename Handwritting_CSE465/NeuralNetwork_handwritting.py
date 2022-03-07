<!DOCTYPE html>
<html>
<head><meta charset="utf-8" />

<title>Untitled26</title>

<script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.0.3/jquery.min.js"></script>



<style type="text/css">
    /*!
*
* Twitter Bootstrap
*
*/
/*!
 * Bootstrap v3.3.7 (http://getbootstrap.com)
 * Copyright 2011-2016 Twitter, Inc.
 * Licensed under MIT (https://github.com/twbs/bootstrap/blob/master/LICENSE)
 */
/*! normalize.css v3.0.3 | MIT License | github.com/necolas/normalize.css */
html {
  font-family: sans-serif;
  -ms-text-size-adjust: 100%;
  -webkit-text-size-adjust: 100%;
}
body {
  margin: 0;
}
article,
aside,
details,
figcaption,
figure,
footer,
header,
hgroup,
main,
menu,
nav,
section,
summary {
  display: block;
}
audio,
canvas,
progress,
video {
  display: inline-block;
  vertical-align: baseline;
}
audio:not([controls]) {
  display: none;
  height: 0;
}
[hidden],
template {
  display: none;
}
a {
  background-color: transparent;
}
a:active,
a:hover {
  outline: 0;
}
abbr[title] {
  border-bottom: 1px dotted;
}
b,
strong {
  font-weight: bold;
}
dfn {
  font-style: italic;
}
h1 {
  font-size: 2em;
  margin: 0.67em 0;
}
mark {
  background: #ff0;
  color: #000;
}
small {
  font-size: 80%;
}
sub,
sup {
  font-size: 75%;
  line-height: 0;
  position: relative;
  vertical-align: baseline;
}
sup {
  top: -0.5em;
}
sub {
  bottom: -0.25em;
}
img {
  border: 0;
}
svg:not(:root) {
  overflow: hidden;
}
figure {
  margin: 1em 40px;
}
hr {
  box-sizing: content-box;
  height: 0;
}
pre {
  overflow: auto;
}
code,
kbd,
pre,
samp {
  font-family: monospace, monospace;
  font-size: 1em;
}
button,
input,
optgroup,
select,
textarea {
  color: inherit;
  font: inherit;
  margin: 0;
}
button {
  overflow: visible;
}
button,
select {
  text-transform: none;
}
button,
html input[type="button"],
input[type="reset"],
input[type="submit"] {
  -webkit-appearance: button;
  cursor: pointer;
}
button[disabled],
html input[disabled] {
  cursor: default;
}
button::-moz-focus-inner,
input::-moz-focus-inner {
  border: 0;
  padding: 0;
}
input {
  line-height: normal;
}
input[type="checkbox"],
input[type="radio"] {
  box-sizing: border-box;
  padding: 0;
}
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: textfield;
  box-sizing: content-box;
}
input[type="search"]::-webkit-search-cancel-button,
input[type="search"]::-webkit-search-decoration {
  -webkit-appearance: none;
}
fieldset {
  border: 1px solid #c0c0c0;
  margin: 0 2px;
  padding: 0.35em 0.625em 0.75em;
}
legend {
  border: 0;
  padding: 0;
}
textarea {
  overflow: auto;
}
optgroup {
  font-weight: bold;
}
table {
  border-collapse: collapse;
  border-spacing: 0;
}
td,
th {
  padding: 0;
}
/*! Source: https://github.com/h5bp/html5-boilerplate/blob/master/src/css/main.css */
@media print {
  *,
  *:before,
  *:after {
    background: transparent !important;
    box-shadow: none !important;
    text-shadow: none !important;
  }
  a,
  a:visited {
    text-decoration: underline;
  }
  a[href]:after {
    content: " (" attr(href) ")";
  }
  abbr[title]:after {
    content: " (" attr(title) ")";
  }
  a[href^="#"]:after,
  a[href^="javascript:"]:after {
    content: "";
  }
  pre,
  blockquote {
    border: 1px solid #999;
    page-break-inside: avoid;
  }
  thead {
    display: table-header-group;
  }
  tr,
  img {
    page-break-inside: avoid;
  }
  img {
    max-width: 100% !important;
  }
  p,
  h2,
  h3 {
    orphans: 3;
    widows: 3;
  }
  h2,
  h3 {
    page-break-after: avoid;
  }
  .navbar {
    display: none;
  }
  .btn > .caret,
  .dropup > .btn > .caret {
    border-top-color: #000 !important;
  }
  .label {
    border: 1px solid #000;
  }
  .table {
    border-collapse: collapse !important;
  }
  .table td,
  .table th {
    background-color: #fff !important;
  }
  .table-bordered th,
  .table-bordered td {
    border: 1px solid #ddd !important;
  }
}
@font-face {
  font-family: 'Glyphicons Halflings';
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot');
  src: url('../components/bootstrap/fonts/glyphicons-halflings-regular.eot?#iefix') format('embedded-opentype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff2') format('woff2'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.woff') format('woff'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.ttf') format('truetype'), url('../components/bootstrap/fonts/glyphicons-halflings-regular.svg#glyphicons_halflingsregular') format('svg');
}
.glyphicon {
  position: relative;
  top: 1px;
  display: inline-block;
  font-family: 'Glyphicons Halflings';
  font-style: normal;
  font-weight: normal;
  line-height: 1;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
.glyphicon-asterisk:before {
  content: "\002a";
}
.glyphicon-plus:before {
  content: "\002b";
}
.glyphicon-euro:before,
.glyphicon-eur:before {
  content: "\20ac";
}
.glyphicon-minus:before {
  content: "\2212";
}
.glyphicon-cloud:before {
  content: "\2601";
}
.glyphicon-envelope:before {
  content: "\2709";
}
.glyphicon-pencil:before {
  content: "\270f";
}
.glyphicon-glass:before {
  content: "\e001";
}
.glyphicon-music:before {
  content: "\e002";
}
.glyphicon-search:before {
  content: "\e003";
}
.glyphicon-heart:before {
  content: "\e005";
}
.glyphicon-star:before {
  content: "\e006";
}
.glyphicon-star-empty:before {
  content: "\e007";
}
.glyphicon-user:before {
  content: "\e008";
}
.glyphicon-film:before {
  content: "\e009";
}
.glyphicon-th-large:before {
  content: "\e010";
}
.glyphicon-th:before {
  content: "\e011";
}
.glyphicon-th-list:before {
  content: "\e012";
}
.glyphicon-ok:before {
  content: "\e013";
}
.glyphicon-remove:before {
  content: "\e014";
}
.glyphicon-zoom-in:before {
  content: "\e015";
}
.glyphicon-zoom-out:before {
  content: "\e016";
}
.glyphicon-off:before {
  content: "\e017";
}
.glyphicon-signal:before {
  content: "\e018";
}
.glyphicon-cog:before {
  content: "\e019";
}
.glyphicon-trash:before {
  content: "\e020";
}
.glyphicon-home:before {
  content: "\e021";
}
.glyphicon-file:before {
  content: "\e022";
}
.glyphicon-time:before {
  content: "\e023";
}
.glyphicon-road:before {
  content: "\e024";
}
.glyphicon-download-alt:before {
  content: "\e025";
}
.glyphicon-download:before {
  content: "\e026";
}
.glyphicon-upload:before {
  content: "\e027";
}
.glyphicon-inbox:before {
  content: "\e028";
}
.glyphicon-play-circle:before {
  content: "\e029";
}
.glyphicon-repeat:before {
  content: "\e030";
}
.glyphicon-refresh:before {
  content: "\e031";
}
.glyphicon-list-alt:before {
  content: "\e032";
}
.glyphicon-lock:before {
  content: "\e033";
}
.glyphicon-flag:before {
  content: "\e034";
}
.glyphicon-headphones:before {
  content: "\e035";
}
.glyphicon-volume-off:before {
  content: "\e036";
}
.glyphicon-volume-down:before {
  content: "\e037";
}
.glyphicon-volume-up:before {
  content: "\e038";
}
.glyphicon-qrcode:before {
  content: "\e039";
}
.glyphicon-barcode:before {
  content: "\e040";
}
.glyphicon-tag:before {
  content: "\e041";
}
.glyphicon-tags:before {
  content: "\e042";
}
.glyphicon-book:before {
  content: "\e043";
}
.glyphicon-bookmark:before {
  content: "\e044";
}
.glyphicon-print:before {
  content: "\e045";
}
.glyphicon-camera:before {
  content: "\e046";
}
.glyphicon-font:before {
  content: "\e047";
}
.glyphicon-bold:before {
  content: "\e048";
}
.glyphicon-italic:before {
  content: "\e049";
}
.glyphicon-text-height:before {
  content: "\e050";
}
.glyphicon-text-width:before {
  content: "\e051";
}
.glyphicon-align-left:before {
  content: "\e052";
}
.glyphicon-align-center:before {
  content: "\e053";
}
.glyphicon-align-right:before {
  content: "\e054";
}
.glyphicon-align-justify:before {
  content: "\e055";
}
.glyphicon-list:before {
  content: "\e056";
}
.glyphicon-indent-left:before {
  content: "\e057";
}
.glyphicon-indent-right:before {
  content: "\e058";
}
.glyphicon-facetime-video:before {
  content: "\e059";
}
.glyphicon-picture:before {
  content: "\e060";
}
.glyphicon-map-marker:before {
  content: "\e062";
}
.glyphicon-adjust:before {
  content: "\e063";
}
.glyphicon-tint:before {
  content: "\e064";
}
.glyphicon-edit:before {
  content: "\e065";
}
.glyphicon-share:before {
  content: "\e066";
}
.glyphicon-check:before {
  content: "\e067";
}
.glyphicon-move:before {
  content: "\e068";
}
.glyphicon-step-backward:before {
  content: "\e069";
}
.glyphicon-fast-backward:before {
  content: "\e070";
}
.glyphicon-backward:before {
  content: "\e071";
}
.glyphicon-play:before {
  content: "\e072";
}
.glyphicon-pause:before {
  content: "\e073";
}
.glyphicon-stop:before {
  content: "\e074";
}
.glyphicon-forward:before {
  content: "\e075";
}
.glyphicon-fast-forward:before {
  content: "\e076";
}
.glyphicon-step-forward:before {
  content: "\e077";
}
.glyphicon-eject:before {
  content: "\e078";
}
.glyphicon-chevron-left:before {
  content: "\e079";
}
.glyphicon-chevron-right:before {
  content: "\e080";
}
.glyphicon-plus-sign:before {
  content: "\e081";
}
.glyphicon-minus-sign:before {
  content: "\e082";
}
.glyphicon-remove-sign:before {
  content: "\e083";
}
.glyphicon-ok-sign:before {
  content: "\e084";
}
.glyphicon-question-sign:before {
  content: "\e085";
}
.glyphicon-info-sign:before {
  content: "\e086";
}
.glyphicon-screenshot:before {
  content: "\e087";
}
.glyphicon-remove-circle:before {
  content: "\e088";
}
.glyphicon-ok-circle:before {
  content: "\e089";
}
.glyphicon-ban-circle:before {
  content: "\e090";
}
.glyphicon-arrow-left:before {
  content: "\e091";
}
.glyphicon-arrow-right:before {
  content: "\e092";
}
.glyphicon-arrow-up:before {
  content: "\e093";
}
.glyphicon-arrow-down:before {
  content: "\e094";
}
.glyphicon-share-alt:before {
  content: "\e095";
}
.glyphicon-resize-full:before {
  content: "\e096";
}
.glyphicon-resize-small:before {
  content: "\e097";
}
.glyphicon-exclamation-sign:before {
  content: "\e101";
}
.glyphicon-gift:before {
  content: "\e102";
}
.glyphicon-leaf:before {
  content: "\e103";
}
.glyphicon-fire:before {
  content: "\e104";
}
.glyphicon-eye-open:before {
  content: "\e105";
}
.glyphicon-eye-close:before {
  content: "\e106";
}
.glyphicon-warning-sign:before {
  content: "\e107";
}
.glyphicon-plane:before {
  content: "\e108";
}
.glyphicon-calendar:before {
  content: "\e109";
}
.glyphicon-random:before {
  content: "\e110";
}
.glyphicon-comment:before {
  content: "\e111";
}
.glyphicon-magnet:before {
  content: "\e112";
}
.glyphicon-chevron-up:before {
  content: "\e113";
}
.glyphicon-chevron-down:before {
  content: "\e114";
}
.glyphicon-retweet:before {
  content: "\e115";
}
.glyphicon-shopping-cart:before {
  content: "\e116";
}
.glyphicon-folder-close:before {
  content: "\e117";
}
.glyphicon-folder-open:before {
  content: "\e118";
}
.glyphicon-resize-vertical:before {
  content: "\e119";
}
.glyphicon-resize-horizontal:before {
  content: "\e120";
}
.glyphicon-hdd:before {
  content: "\e121";
}
.glyphicon-bullhorn:before {
  content: "\e122";
}
.glyphicon-bell:before {
  content: "\e123";
}
.glyphicon-certificate:before {
  content: "\e124";
}
.glyphicon-thumbs-up:before {
  content: "\e125";
}
.glyphicon-thumbs-down:before {
  content: "\e126";
}
.glyphicon-hand-right:before {
  content: "\e127";
}
.glyphicon-hand-left:before {
  content: "\e128";
}
.glyphicon-hand-up:before {
  content: "\e129";
}
.glyphicon-hand-down:before {
  content: "\e130";
}
.glyphicon-circle-arrow-right:before {
  content: "\e131";
}
.glyphicon-circle-arrow-left:before {
  content: "\e132";
}
.glyphicon-circle-arrow-up:before {
  content: "\e133";
}
.glyphicon-circle-arrow-down:before {
  content: "\e134";
}
.glyphicon-globe:before {
  content: "\e135";
}
.glyphicon-wrench:before {
  content: "\e136";
}
.glyphicon-tasks:before {
  content: "\e137";
}
.glyphicon-filter:before {
  content: "\e138";
}
.glyphicon-briefcase:before {
  content: "\e139";
}
.glyphicon-fullscreen:before {
  content: "\e140";
}
.glyphicon-dashboard:before {
  content: "\e141";
}
.glyphicon-paperclip:before {
  content: "\e142";
}
.glyphicon-heart-empty:before {
  content: "\e143";
}
.glyphicon-link:before {
  content: "\e144";
}
.glyphicon-phone:before {
  content: "\e145";
}
.glyphicon-pushpin:before {
  content: "\e146";
}
.glyphicon-usd:before {
  content: "\e148";
}
.glyphicon-gbp:before {
  content: "\e149";
}
.glyphicon-sort:before {
  content: "\e150";
}
.glyphicon-sort-by-alphabet:before {
  content: "\e151";
}
.glyphicon-sort-by-alphabet-alt:before {
  content: "\e152";
}
.glyphicon-sort-by-order:before {
  content: "\e153";
}
.glyphicon-sort-by-order-alt:before {
  content: "\e154";
}
.glyphicon-sort-by-attributes:before {
  content: "\e155";
}
.glyphicon-sort-by-attributes-alt:before {
  content: "\e156";
}
.glyphicon-unchecked:before {
  content: "\e157";
}
.glyphicon-expand:before {
  content: "\e158";
}
.glyphicon-collapse-down:before {
  content: "\e159";
}
.glyphicon-collapse-up:before {
  content: "\e160";
}
.glyphicon-log-in:before {
  content: "\e161";
}
.glyphicon-flash:before {
  content: "\e162";
}
.glyphicon-log-out:before {
  content: "\e163";
}
.glyphicon-new-window:before {
  content: "\e164";
}
.glyphicon-record:before {
  content: "\e165";
}
.glyphicon-save:before {
  content: "\e166";
}
.glyphicon-open:before {
  content: "\e167";
}
.glyphicon-saved:before {
  content: "\e168";
}
.glyphicon-import:before {
  content: "\e169";
}
.glyphicon-export:before {
  content: "\e170";
}
.glyphicon-send:before {
  content: "\e171";
}
.glyphicon-floppy-disk:before {
  content: "\e172";
}
.glyphicon-floppy-saved:before {
  content: "\e173";
}
.glyphicon-floppy-remove:before {
  content: "\e174";
}
.glyphicon-floppy-save:before {
  content: "\e175";
}
.glyphicon-floppy-open:before {
  content: "\e176";
}
.glyphicon-credit-card:before {
  content: "\e177";
}
.glyphicon-transfer:before {
  content: "\e178";
}
.glyphicon-cutlery:before {
  content: "\e179";
}
.glyphicon-header:before {
  content: "\e180";
}
.glyphicon-compressed:before {
  content: "\e181";
}
.glyphicon-earphone:before {
  content: "\e182";
}
.glyphicon-phone-alt:before {
  content: "\e183";
}
.glyphicon-tower:before {
  content: "\e184";
}
.glyphicon-stats:before {
  content: "\e185";
}
.glyphicon-sd-video:before {
  content: "\e186";
}
.glyphicon-hd-video:before {
  content: "\e187";
}
.glyphicon-subtitles:before {
  content: "\e188";
}
.glyphicon-sound-stereo:before {
  content: "\e189";
}
.glyphicon-sound-dolby:before {
  content: "\e190";
}
.glyphicon-sound-5-1:before {
  content: "\e191";
}
.glyphicon-sound-6-1:before {
  content: "\e192";
}
.glyphicon-sound-7-1:before {
  content: "\e193";
}
.glyphicon-copyright-mark:before {
  content: "\e194";
}
.glyphicon-registration-mark:before {
  content: "\e195";
}
.glyphicon-cloud-download:before {
  content: "\e197";
}
.glyphicon-cloud-upload:before {
  content: "\e198";
}
.glyphicon-tree-conifer:before {
  content: "\e199";
}
.glyphicon-tree-deciduous:before {
  content: "\e200";
}
.glyphicon-cd:before {
  content: "\e201";
}
.glyphicon-save-file:before {
  content: "\e202";
}
.glyphicon-open-file:before {
  content: "\e203";
}
.glyphicon-level-up:before {
  content: "\e204";
}
.glyphicon-copy:before {
  content: "\e205";
}
.glyphicon-paste:before {
  content: "\e206";
}
.glyphicon-alert:before {
  content: "\e209";
}
.glyphicon-equalizer:before {
  content: "\e210";
}
.glyphicon-king:before {
  content: "\e211";
}
.glyphicon-queen:before {
  content: "\e212";
}
.glyphicon-pawn:before {
  content: "\e213";
}
.glyphicon-bishop:before {
  content: "\e214";
}
.glyphicon-knight:before {
  content: "\e215";
}
.glyphicon-baby-formula:before {
  content: "\e216";
}
.glyphicon-tent:before {
  content: "\26fa";
}
.glyphicon-blackboard:before {
  content: "\e218";
}
.glyphicon-bed:before {
  content: "\e219";
}
.glyphicon-apple:before {
  content: "\f8ff";
}
.glyphicon-erase:before {
  content: "\e221";
}
.glyphicon-hourglass:before {
  content: "\231b";
}
.glyphicon-lamp:before {
  content: "\e223";
}
.glyphicon-duplicate:before {
  content: "\e224";
}
.glyphicon-piggy-bank:before {
  content: "\e225";
}
.glyphicon-scissors:before {
  content: "\e226";
}
.glyphicon-bitcoin:before {
  content: "\e227";
}
.glyphicon-btc:before {
  content: "\e227";
}
.glyphicon-xbt:before {
  content: "\e227";
}
.glyphicon-yen:before {
  content: "\00a5";
}
.glyphicon-jpy:before {
  content: "\00a5";
}
.glyphicon-ruble:before {
  content: "\20bd";
}
.glyphicon-rub:before {
  content: "\20bd";
}
.glyphicon-scale:before {
  content: "\e230";
}
.glyphicon-ice-lolly:before {
  content: "\e231";
}
.glyphicon-ice-lolly-tasted:before {
  content: "\e232";
}
.glyphicon-education:before {
  content: "\e233";
}
.glyphicon-option-horizontal:before {
  content: "\e234";
}
.glyphicon-option-vertical:before {
  content: "\e235";
}
.glyphicon-menu-hamburger:before {
  content: "\e236";
}
.glyphicon-modal-window:before {
  content: "\e237";
}
.glyphicon-oil:before {
  content: "\e238";
}
.glyphicon-grain:before {
  content: "\e239";
}
.glyphicon-sunglasses:before {
  content: "\e240";
}
.glyphicon-text-size:before {
  content: "\e241";
}
.glyphicon-text-color:before {
  content: "\e242";
}
.glyphicon-text-background:before {
  content: "\e243";
}
.glyphicon-object-align-top:before {
  content: "\e244";
}
.glyphicon-object-align-bottom:before {
  content: "\e245";
}
.glyphicon-object-align-horizontal:before {
  content: "\e246";
}
.glyphicon-object-align-left:before {
  content: "\e247";
}
.glyphicon-object-align-vertical:before {
  content: "\e248";
}
.glyphicon-object-align-right:before {
  content: "\e249";
}
.glyphicon-triangle-right:before {
  content: "\e250";
}
.glyphicon-triangle-left:before {
  content: "\e251";
}
.glyphicon-triangle-bottom:before {
  content: "\e252";
}
.glyphicon-triangle-top:before {
  content: "\e253";
}
.glyphicon-console:before {
  content: "\e254";
}
.glyphicon-superscript:before {
  content: "\e255";
}
.glyphicon-subscript:before {
  content: "\e256";
}
.glyphicon-menu-left:before {
  content: "\e257";
}
.glyphicon-menu-right:before {
  content: "\e258";
}
.glyphicon-menu-down:before {
  content: "\e259";
}
.glyphicon-menu-up:before {
  content: "\e260";
}
* {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
*:before,
*:after {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
html {
  font-size: 10px;
  -webkit-tap-highlight-color: rgba(0, 0, 0, 0);
}
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 13px;
  line-height: 1.42857143;
  color: #000;
  background-color: #fff;
}
input,
button,
select,
textarea {
  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
}
a {
  color: #337ab7;
  text-decoration: none;
}
a:hover,
a:focus {
  color: #23527c;
  text-decoration: underline;
}
a:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
figure {
  margin: 0;
}
img {
  vertical-align: middle;
}
.img-responsive,
.thumbnail > img,
.thumbnail a > img,
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  display: block;
  max-width: 100%;
  height: auto;
}
.img-rounded {
  border-radius: 3px;
}
.img-thumbnail {
  padding: 4px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: all 0.2s ease-in-out;
  -o-transition: all 0.2s ease-in-out;
  transition: all 0.2s ease-in-out;
  display: inline-block;
  max-width: 100%;
  height: auto;
}
.img-circle {
  border-radius: 50%;
}
hr {
  margin-top: 18px;
  margin-bottom: 18px;
  border: 0;
  border-top: 1px solid #eeeeee;
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
[role="button"] {
  cursor: pointer;
}
h1,
h2,
h3,
h4,
h5,
h6,
.h1,
.h2,
.h3,
.h4,
.h5,
.h6 {
  font-family: inherit;
  font-weight: 500;
  line-height: 1.1;
  color: inherit;
}
h1 small,
h2 small,
h3 small,
h4 small,
h5 small,
h6 small,
.h1 small,
.h2 small,
.h3 small,
.h4 small,
.h5 small,
.h6 small,
h1 .small,
h2 .small,
h3 .small,
h4 .small,
h5 .small,
h6 .small,
.h1 .small,
.h2 .small,
.h3 .small,
.h4 .small,
.h5 .small,
.h6 .small {
  font-weight: normal;
  line-height: 1;
  color: #777777;
}
h1,
.h1,
h2,
.h2,
h3,
.h3 {
  margin-top: 18px;
  margin-bottom: 9px;
}
h1 small,
.h1 small,
h2 small,
.h2 small,
h3 small,
.h3 small,
h1 .small,
.h1 .small,
h2 .small,
.h2 .small,
h3 .small,
.h3 .small {
  font-size: 65%;
}
h4,
.h4,
h5,
.h5,
h6,
.h6 {
  margin-top: 9px;
  margin-bottom: 9px;
}
h4 small,
.h4 small,
h5 small,
.h5 small,
h6 small,
.h6 small,
h4 .small,
.h4 .small,
h5 .small,
.h5 .small,
h6 .small,
.h6 .small {
  font-size: 75%;
}
h1,
.h1 {
  font-size: 33px;
}
h2,
.h2 {
  font-size: 27px;
}
h3,
.h3 {
  font-size: 23px;
}
h4,
.h4 {
  font-size: 17px;
}
h5,
.h5 {
  font-size: 13px;
}
h6,
.h6 {
  font-size: 12px;
}
p {
  margin: 0 0 9px;
}
.lead {
  margin-bottom: 18px;
  font-size: 14px;
  font-weight: 300;
  line-height: 1.4;
}
@media (min-width: 768px) {
  .lead {
    font-size: 19.5px;
  }
}
small,
.small {
  font-size: 92%;
}
mark,
.mark {
  background-color: #fcf8e3;
  padding: .2em;
}
.text-left {
  text-align: left;
}
.text-right {
  text-align: right;
}
.text-center {
  text-align: center;
}
.text-justify {
  text-align: justify;
}
.text-nowrap {
  white-space: nowrap;
}
.text-lowercase {
  text-transform: lowercase;
}
.text-uppercase {
  text-transform: uppercase;
}
.text-capitalize {
  text-transform: capitalize;
}
.text-muted {
  color: #777777;
}
.text-primary {
  color: #337ab7;
}
a.text-primary:hover,
a.text-primary:focus {
  color: #286090;
}
.text-success {
  color: #3c763d;
}
a.text-success:hover,
a.text-success:focus {
  color: #2b542c;
}
.text-info {
  color: #31708f;
}
a.text-info:hover,
a.text-info:focus {
  color: #245269;
}
.text-warning {
  color: #8a6d3b;
}
a.text-warning:hover,
a.text-warning:focus {
  color: #66512c;
}
.text-danger {
  color: #a94442;
}
a.text-danger:hover,
a.text-danger:focus {
  color: #843534;
}
.bg-primary {
  color: #fff;
  background-color: #337ab7;
}
a.bg-primary:hover,
a.bg-primary:focus {
  background-color: #286090;
}
.bg-success {
  background-color: #dff0d8;
}
a.bg-success:hover,
a.bg-success:focus {
  background-color: #c1e2b3;
}
.bg-info {
  background-color: #d9edf7;
}
a.bg-info:hover,
a.bg-info:focus {
  background-color: #afd9ee;
}
.bg-warning {
  background-color: #fcf8e3;
}
a.bg-warning:hover,
a.bg-warning:focus {
  background-color: #f7ecb5;
}
.bg-danger {
  background-color: #f2dede;
}
a.bg-danger:hover,
a.bg-danger:focus {
  background-color: #e4b9b9;
}
.page-header {
  padding-bottom: 8px;
  margin: 36px 0 18px;
  border-bottom: 1px solid #eeeeee;
}
ul,
ol {
  margin-top: 0;
  margin-bottom: 9px;
}
ul ul,
ol ul,
ul ol,
ol ol {
  margin-bottom: 0;
}
.list-unstyled {
  padding-left: 0;
  list-style: none;
}
.list-inline {
  padding-left: 0;
  list-style: none;
  margin-left: -5px;
}
.list-inline > li {
  display: inline-block;
  padding-left: 5px;
  padding-right: 5px;
}
dl {
  margin-top: 0;
  margin-bottom: 18px;
}
dt,
dd {
  line-height: 1.42857143;
}
dt {
  font-weight: bold;
}
dd {
  margin-left: 0;
}
@media (min-width: 541px) {
  .dl-horizontal dt {
    float: left;
    width: 160px;
    clear: left;
    text-align: right;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  .dl-horizontal dd {
    margin-left: 180px;
  }
}
abbr[title],
abbr[data-original-title] {
  cursor: help;
  border-bottom: 1px dotted #777777;
}
.initialism {
  font-size: 90%;
  text-transform: uppercase;
}
blockquote {
  padding: 9px 18px;
  margin: 0 0 18px;
  font-size: inherit;
  border-left: 5px solid #eeeeee;
}
blockquote p:last-child,
blockquote ul:last-child,
blockquote ol:last-child {
  margin-bottom: 0;
}
blockquote footer,
blockquote small,
blockquote .small {
  display: block;
  font-size: 80%;
  line-height: 1.42857143;
  color: #777777;
}
blockquote footer:before,
blockquote small:before,
blockquote .small:before {
  content: '\2014 \00A0';
}
.blockquote-reverse,
blockquote.pull-right {
  padding-right: 15px;
  padding-left: 0;
  border-right: 5px solid #eeeeee;
  border-left: 0;
  text-align: right;
}
.blockquote-reverse footer:before,
blockquote.pull-right footer:before,
.blockquote-reverse small:before,
blockquote.pull-right small:before,
.blockquote-reverse .small:before,
blockquote.pull-right .small:before {
  content: '';
}
.blockquote-reverse footer:after,
blockquote.pull-right footer:after,
.blockquote-reverse small:after,
blockquote.pull-right small:after,
.blockquote-reverse .small:after,
blockquote.pull-right .small:after {
  content: '\00A0 \2014';
}
address {
  margin-bottom: 18px;
  font-style: normal;
  line-height: 1.42857143;
}
code,
kbd,
pre,
samp {
  font-family: monospace;
}
code {
  padding: 2px 4px;
  font-size: 90%;
  color: #c7254e;
  background-color: #f9f2f4;
  border-radius: 2px;
}
kbd {
  padding: 2px 4px;
  font-size: 90%;
  color: #888;
  background-color: transparent;
  border-radius: 1px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
}
kbd kbd {
  padding: 0;
  font-size: 100%;
  font-weight: bold;
  box-shadow: none;
}
pre {
  display: block;
  padding: 8.5px;
  margin: 0 0 9px;
  font-size: 12px;
  line-height: 1.42857143;
  word-break: break-all;
  word-wrap: break-word;
  color: #333333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
  border-radius: 2px;
}
pre code {
  padding: 0;
  font-size: inherit;
  color: inherit;
  white-space: pre-wrap;
  background-color: transparent;
  border-radius: 0;
}
.pre-scrollable {
  max-height: 340px;
  overflow-y: scroll;
}
.container {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
@media (min-width: 768px) {
  .container {
    width: 768px;
  }
}
@media (min-width: 992px) {
  .container {
    width: 940px;
  }
}
@media (min-width: 1200px) {
  .container {
    width: 1140px;
  }
}
.container-fluid {
  margin-right: auto;
  margin-left: auto;
  padding-left: 0px;
  padding-right: 0px;
}
.row {
  margin-left: 0px;
  margin-right: 0px;
}
.col-xs-1, .col-sm-1, .col-md-1, .col-lg-1, .col-xs-2, .col-sm-2, .col-md-2, .col-lg-2, .col-xs-3, .col-sm-3, .col-md-3, .col-lg-3, .col-xs-4, .col-sm-4, .col-md-4, .col-lg-4, .col-xs-5, .col-sm-5, .col-md-5, .col-lg-5, .col-xs-6, .col-sm-6, .col-md-6, .col-lg-6, .col-xs-7, .col-sm-7, .col-md-7, .col-lg-7, .col-xs-8, .col-sm-8, .col-md-8, .col-lg-8, .col-xs-9, .col-sm-9, .col-md-9, .col-lg-9, .col-xs-10, .col-sm-10, .col-md-10, .col-lg-10, .col-xs-11, .col-sm-11, .col-md-11, .col-lg-11, .col-xs-12, .col-sm-12, .col-md-12, .col-lg-12 {
  position: relative;
  min-height: 1px;
  padding-left: 0px;
  padding-right: 0px;
}
.col-xs-1, .col-xs-2, .col-xs-3, .col-xs-4, .col-xs-5, .col-xs-6, .col-xs-7, .col-xs-8, .col-xs-9, .col-xs-10, .col-xs-11, .col-xs-12 {
  float: left;
}
.col-xs-12 {
  width: 100%;
}
.col-xs-11 {
  width: 91.66666667%;
}
.col-xs-10 {
  width: 83.33333333%;
}
.col-xs-9 {
  width: 75%;
}
.col-xs-8 {
  width: 66.66666667%;
}
.col-xs-7 {
  width: 58.33333333%;
}
.col-xs-6 {
  width: 50%;
}
.col-xs-5 {
  width: 41.66666667%;
}
.col-xs-4 {
  width: 33.33333333%;
}
.col-xs-3 {
  width: 25%;
}
.col-xs-2 {
  width: 16.66666667%;
}
.col-xs-1 {
  width: 8.33333333%;
}
.col-xs-pull-12 {
  right: 100%;
}
.col-xs-pull-11 {
  right: 91.66666667%;
}
.col-xs-pull-10 {
  right: 83.33333333%;
}
.col-xs-pull-9 {
  right: 75%;
}
.col-xs-pull-8 {
  right: 66.66666667%;
}
.col-xs-pull-7 {
  right: 58.33333333%;
}
.col-xs-pull-6 {
  right: 50%;
}
.col-xs-pull-5 {
  right: 41.66666667%;
}
.col-xs-pull-4 {
  right: 33.33333333%;
}
.col-xs-pull-3 {
  right: 25%;
}
.col-xs-pull-2 {
  right: 16.66666667%;
}
.col-xs-pull-1 {
  right: 8.33333333%;
}
.col-xs-pull-0 {
  right: auto;
}
.col-xs-push-12 {
  left: 100%;
}
.col-xs-push-11 {
  left: 91.66666667%;
}
.col-xs-push-10 {
  left: 83.33333333%;
}
.col-xs-push-9 {
  left: 75%;
}
.col-xs-push-8 {
  left: 66.66666667%;
}
.col-xs-push-7 {
  left: 58.33333333%;
}
.col-xs-push-6 {
  left: 50%;
}
.col-xs-push-5 {
  left: 41.66666667%;
}
.col-xs-push-4 {
  left: 33.33333333%;
}
.col-xs-push-3 {
  left: 25%;
}
.col-xs-push-2 {
  left: 16.66666667%;
}
.col-xs-push-1 {
  left: 8.33333333%;
}
.col-xs-push-0 {
  left: auto;
}
.col-xs-offset-12 {
  margin-left: 100%;
}
.col-xs-offset-11 {
  margin-left: 91.66666667%;
}
.col-xs-offset-10 {
  margin-left: 83.33333333%;
}
.col-xs-offset-9 {
  margin-left: 75%;
}
.col-xs-offset-8 {
  margin-left: 66.66666667%;
}
.col-xs-offset-7 {
  margin-left: 58.33333333%;
}
.col-xs-offset-6 {
  margin-left: 50%;
}
.col-xs-offset-5 {
  margin-left: 41.66666667%;
}
.col-xs-offset-4 {
  margin-left: 33.33333333%;
}
.col-xs-offset-3 {
  margin-left: 25%;
}
.col-xs-offset-2 {
  margin-left: 16.66666667%;
}
.col-xs-offset-1 {
  margin-left: 8.33333333%;
}
.col-xs-offset-0 {
  margin-left: 0%;
}
@media (min-width: 768px) {
  .col-sm-1, .col-sm-2, .col-sm-3, .col-sm-4, .col-sm-5, .col-sm-6, .col-sm-7, .col-sm-8, .col-sm-9, .col-sm-10, .col-sm-11, .col-sm-12 {
    float: left;
  }
  .col-sm-12 {
    width: 100%;
  }
  .col-sm-11 {
    width: 91.66666667%;
  }
  .col-sm-10 {
    width: 83.33333333%;
  }
  .col-sm-9 {
    width: 75%;
  }
  .col-sm-8 {
    width: 66.66666667%;
  }
  .col-sm-7 {
    width: 58.33333333%;
  }
  .col-sm-6 {
    width: 50%;
  }
  .col-sm-5 {
    width: 41.66666667%;
  }
  .col-sm-4 {
    width: 33.33333333%;
  }
  .col-sm-3 {
    width: 25%;
  }
  .col-sm-2 {
    width: 16.66666667%;
  }
  .col-sm-1 {
    width: 8.33333333%;
  }
  .col-sm-pull-12 {
    right: 100%;
  }
  .col-sm-pull-11 {
    right: 91.66666667%;
  }
  .col-sm-pull-10 {
    right: 83.33333333%;
  }
  .col-sm-pull-9 {
    right: 75%;
  }
  .col-sm-pull-8 {
    right: 66.66666667%;
  }
  .col-sm-pull-7 {
    right: 58.33333333%;
  }
  .col-sm-pull-6 {
    right: 50%;
  }
  .col-sm-pull-5 {
    right: 41.66666667%;
  }
  .col-sm-pull-4 {
    right: 33.33333333%;
  }
  .col-sm-pull-3 {
    right: 25%;
  }
  .col-sm-pull-2 {
    right: 16.66666667%;
  }
  .col-sm-pull-1 {
    right: 8.33333333%;
  }
  .col-sm-pull-0 {
    right: auto;
  }
  .col-sm-push-12 {
    left: 100%;
  }
  .col-sm-push-11 {
    left: 91.66666667%;
  }
  .col-sm-push-10 {
    left: 83.33333333%;
  }
  .col-sm-push-9 {
    left: 75%;
  }
  .col-sm-push-8 {
    left: 66.66666667%;
  }
  .col-sm-push-7 {
    left: 58.33333333%;
  }
  .col-sm-push-6 {
    left: 50%;
  }
  .col-sm-push-5 {
    left: 41.66666667%;
  }
  .col-sm-push-4 {
    left: 33.33333333%;
  }
  .col-sm-push-3 {
    left: 25%;
  }
  .col-sm-push-2 {
    left: 16.66666667%;
  }
  .col-sm-push-1 {
    left: 8.33333333%;
  }
  .col-sm-push-0 {
    left: auto;
  }
  .col-sm-offset-12 {
    margin-left: 100%;
  }
  .col-sm-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-sm-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-sm-offset-9 {
    margin-left: 75%;
  }
  .col-sm-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-sm-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-sm-offset-6 {
    margin-left: 50%;
  }
  .col-sm-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-sm-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-sm-offset-3 {
    margin-left: 25%;
  }
  .col-sm-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-sm-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-sm-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 992px) {
  .col-md-1, .col-md-2, .col-md-3, .col-md-4, .col-md-5, .col-md-6, .col-md-7, .col-md-8, .col-md-9, .col-md-10, .col-md-11, .col-md-12 {
    float: left;
  }
  .col-md-12 {
    width: 100%;
  }
  .col-md-11 {
    width: 91.66666667%;
  }
  .col-md-10 {
    width: 83.33333333%;
  }
  .col-md-9 {
    width: 75%;
  }
  .col-md-8 {
    width: 66.66666667%;
  }
  .col-md-7 {
    width: 58.33333333%;
  }
  .col-md-6 {
    width: 50%;
  }
  .col-md-5 {
    width: 41.66666667%;
  }
  .col-md-4 {
    width: 33.33333333%;
  }
  .col-md-3 {
    width: 25%;
  }
  .col-md-2 {
    width: 16.66666667%;
  }
  .col-md-1 {
    width: 8.33333333%;
  }
  .col-md-pull-12 {
    right: 100%;
  }
  .col-md-pull-11 {
    right: 91.66666667%;
  }
  .col-md-pull-10 {
    right: 83.33333333%;
  }
  .col-md-pull-9 {
    right: 75%;
  }
  .col-md-pull-8 {
    right: 66.66666667%;
  }
  .col-md-pull-7 {
    right: 58.33333333%;
  }
  .col-md-pull-6 {
    right: 50%;
  }
  .col-md-pull-5 {
    right: 41.66666667%;
  }
  .col-md-pull-4 {
    right: 33.33333333%;
  }
  .col-md-pull-3 {
    right: 25%;
  }
  .col-md-pull-2 {
    right: 16.66666667%;
  }
  .col-md-pull-1 {
    right: 8.33333333%;
  }
  .col-md-pull-0 {
    right: auto;
  }
  .col-md-push-12 {
    left: 100%;
  }
  .col-md-push-11 {
    left: 91.66666667%;
  }
  .col-md-push-10 {
    left: 83.33333333%;
  }
  .col-md-push-9 {
    left: 75%;
  }
  .col-md-push-8 {
    left: 66.66666667%;
  }
  .col-md-push-7 {
    left: 58.33333333%;
  }
  .col-md-push-6 {
    left: 50%;
  }
  .col-md-push-5 {
    left: 41.66666667%;
  }
  .col-md-push-4 {
    left: 33.33333333%;
  }
  .col-md-push-3 {
    left: 25%;
  }
  .col-md-push-2 {
    left: 16.66666667%;
  }
  .col-md-push-1 {
    left: 8.33333333%;
  }
  .col-md-push-0 {
    left: auto;
  }
  .col-md-offset-12 {
    margin-left: 100%;
  }
  .col-md-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-md-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-md-offset-9 {
    margin-left: 75%;
  }
  .col-md-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-md-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-md-offset-6 {
    margin-left: 50%;
  }
  .col-md-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-md-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-md-offset-3 {
    margin-left: 25%;
  }
  .col-md-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-md-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-md-offset-0 {
    margin-left: 0%;
  }
}
@media (min-width: 1200px) {
  .col-lg-1, .col-lg-2, .col-lg-3, .col-lg-4, .col-lg-5, .col-lg-6, .col-lg-7, .col-lg-8, .col-lg-9, .col-lg-10, .col-lg-11, .col-lg-12 {
    float: left;
  }
  .col-lg-12 {
    width: 100%;
  }
  .col-lg-11 {
    width: 91.66666667%;
  }
  .col-lg-10 {
    width: 83.33333333%;
  }
  .col-lg-9 {
    width: 75%;
  }
  .col-lg-8 {
    width: 66.66666667%;
  }
  .col-lg-7 {
    width: 58.33333333%;
  }
  .col-lg-6 {
    width: 50%;
  }
  .col-lg-5 {
    width: 41.66666667%;
  }
  .col-lg-4 {
    width: 33.33333333%;
  }
  .col-lg-3 {
    width: 25%;
  }
  .col-lg-2 {
    width: 16.66666667%;
  }
  .col-lg-1 {
    width: 8.33333333%;
  }
  .col-lg-pull-12 {
    right: 100%;
  }
  .col-lg-pull-11 {
    right: 91.66666667%;
  }
  .col-lg-pull-10 {
    right: 83.33333333%;
  }
  .col-lg-pull-9 {
    right: 75%;
  }
  .col-lg-pull-8 {
    right: 66.66666667%;
  }
  .col-lg-pull-7 {
    right: 58.33333333%;
  }
  .col-lg-pull-6 {
    right: 50%;
  }
  .col-lg-pull-5 {
    right: 41.66666667%;
  }
  .col-lg-pull-4 {
    right: 33.33333333%;
  }
  .col-lg-pull-3 {
    right: 25%;
  }
  .col-lg-pull-2 {
    right: 16.66666667%;
  }
  .col-lg-pull-1 {
    right: 8.33333333%;
  }
  .col-lg-pull-0 {
    right: auto;
  }
  .col-lg-push-12 {
    left: 100%;
  }
  .col-lg-push-11 {
    left: 91.66666667%;
  }
  .col-lg-push-10 {
    left: 83.33333333%;
  }
  .col-lg-push-9 {
    left: 75%;
  }
  .col-lg-push-8 {
    left: 66.66666667%;
  }
  .col-lg-push-7 {
    left: 58.33333333%;
  }
  .col-lg-push-6 {
    left: 50%;
  }
  .col-lg-push-5 {
    left: 41.66666667%;
  }
  .col-lg-push-4 {
    left: 33.33333333%;
  }
  .col-lg-push-3 {
    left: 25%;
  }
  .col-lg-push-2 {
    left: 16.66666667%;
  }
  .col-lg-push-1 {
    left: 8.33333333%;
  }
  .col-lg-push-0 {
    left: auto;
  }
  .col-lg-offset-12 {
    margin-left: 100%;
  }
  .col-lg-offset-11 {
    margin-left: 91.66666667%;
  }
  .col-lg-offset-10 {
    margin-left: 83.33333333%;
  }
  .col-lg-offset-9 {
    margin-left: 75%;
  }
  .col-lg-offset-8 {
    margin-left: 66.66666667%;
  }
  .col-lg-offset-7 {
    margin-left: 58.33333333%;
  }
  .col-lg-offset-6 {
    margin-left: 50%;
  }
  .col-lg-offset-5 {
    margin-left: 41.66666667%;
  }
  .col-lg-offset-4 {
    margin-left: 33.33333333%;
  }
  .col-lg-offset-3 {
    margin-left: 25%;
  }
  .col-lg-offset-2 {
    margin-left: 16.66666667%;
  }
  .col-lg-offset-1 {
    margin-left: 8.33333333%;
  }
  .col-lg-offset-0 {
    margin-left: 0%;
  }
}
table {
  background-color: transparent;
}
caption {
  padding-top: 8px;
  padding-bottom: 8px;
  color: #777777;
  text-align: left;
}
th {
  text-align: left;
}
.table {
  width: 100%;
  max-width: 100%;
  margin-bottom: 18px;
}
.table > thead > tr > th,
.table > tbody > tr > th,
.table > tfoot > tr > th,
.table > thead > tr > td,
.table > tbody > tr > td,
.table > tfoot > tr > td {
  padding: 8px;
  line-height: 1.42857143;
  vertical-align: top;
  border-top: 1px solid #ddd;
}
.table > thead > tr > th {
  vertical-align: bottom;
  border-bottom: 2px solid #ddd;
}
.table > caption + thead > tr:first-child > th,
.table > colgroup + thead > tr:first-child > th,
.table > thead:first-child > tr:first-child > th,
.table > caption + thead > tr:first-child > td,
.table > colgroup + thead > tr:first-child > td,
.table > thead:first-child > tr:first-child > td {
  border-top: 0;
}
.table > tbody + tbody {
  border-top: 2px solid #ddd;
}
.table .table {
  background-color: #fff;
}
.table-condensed > thead > tr > th,
.table-condensed > tbody > tr > th,
.table-condensed > tfoot > tr > th,
.table-condensed > thead > tr > td,
.table-condensed > tbody > tr > td,
.table-condensed > tfoot > tr > td {
  padding: 5px;
}
.table-bordered {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > tbody > tr > th,
.table-bordered > tfoot > tr > th,
.table-bordered > thead > tr > td,
.table-bordered > tbody > tr > td,
.table-bordered > tfoot > tr > td {
  border: 1px solid #ddd;
}
.table-bordered > thead > tr > th,
.table-bordered > thead > tr > td {
  border-bottom-width: 2px;
}
.table-striped > tbody > tr:nth-of-type(odd) {
  background-color: #f9f9f9;
}
.table-hover > tbody > tr:hover {
  background-color: #f5f5f5;
}
table col[class*="col-"] {
  position: static;
  float: none;
  display: table-column;
}
table td[class*="col-"],
table th[class*="col-"] {
  position: static;
  float: none;
  display: table-cell;
}
.table > thead > tr > td.active,
.table > tbody > tr > td.active,
.table > tfoot > tr > td.active,
.table > thead > tr > th.active,
.table > tbody > tr > th.active,
.table > tfoot > tr > th.active,
.table > thead > tr.active > td,
.table > tbody > tr.active > td,
.table > tfoot > tr.active > td,
.table > thead > tr.active > th,
.table > tbody > tr.active > th,
.table > tfoot > tr.active > th {
  background-color: #f5f5f5;
}
.table-hover > tbody > tr > td.active:hover,
.table-hover > tbody > tr > th.active:hover,
.table-hover > tbody > tr.active:hover > td,
.table-hover > tbody > tr:hover > .active,
.table-hover > tbody > tr.active:hover > th {
  background-color: #e8e8e8;
}
.table > thead > tr > td.success,
.table > tbody > tr > td.success,
.table > tfoot > tr > td.success,
.table > thead > tr > th.success,
.table > tbody > tr > th.success,
.table > tfoot > tr > th.success,
.table > thead > tr.success > td,
.table > tbody > tr.success > td,
.table > tfoot > tr.success > td,
.table > thead > tr.success > th,
.table > tbody > tr.success > th,
.table > tfoot > tr.success > th {
  background-color: #dff0d8;
}
.table-hover > tbody > tr > td.success:hover,
.table-hover > tbody > tr > th.success:hover,
.table-hover > tbody > tr.success:hover > td,
.table-hover > tbody > tr:hover > .success,
.table-hover > tbody > tr.success:hover > th {
  background-color: #d0e9c6;
}
.table > thead > tr > td.info,
.table > tbody > tr > td.info,
.table > tfoot > tr > td.info,
.table > thead > tr > th.info,
.table > tbody > tr > th.info,
.table > tfoot > tr > th.info,
.table > thead > tr.info > td,
.table > tbody > tr.info > td,
.table > tfoot > tr.info > td,
.table > thead > tr.info > th,
.table > tbody > tr.info > th,
.table > tfoot > tr.info > th {
  background-color: #d9edf7;
}
.table-hover > tbody > tr > td.info:hover,
.table-hover > tbody > tr > th.info:hover,
.table-hover > tbody > tr.info:hover > td,
.table-hover > tbody > tr:hover > .info,
.table-hover > tbody > tr.info:hover > th {
  background-color: #c4e3f3;
}
.table > thead > tr > td.warning,
.table > tbody > tr > td.warning,
.table > tfoot > tr > td.warning,
.table > thead > tr > th.warning,
.table > tbody > tr > th.warning,
.table > tfoot > tr > th.warning,
.table > thead > tr.warning > td,
.table > tbody > tr.warning > td,
.table > tfoot > tr.warning > td,
.table > thead > tr.warning > th,
.table > tbody > tr.warning > th,
.table > tfoot > tr.warning > th {
  background-color: #fcf8e3;
}
.table-hover > tbody > tr > td.warning:hover,
.table-hover > tbody > tr > th.warning:hover,
.table-hover > tbody > tr.warning:hover > td,
.table-hover > tbody > tr:hover > .warning,
.table-hover > tbody > tr.warning:hover > th {
  background-color: #faf2cc;
}
.table > thead > tr > td.danger,
.table > tbody > tr > td.danger,
.table > tfoot > tr > td.danger,
.table > thead > tr > th.danger,
.table > tbody > tr > th.danger,
.table > tfoot > tr > th.danger,
.table > thead > tr.danger > td,
.table > tbody > tr.danger > td,
.table > tfoot > tr.danger > td,
.table > thead > tr.danger > th,
.table > tbody > tr.danger > th,
.table > tfoot > tr.danger > th {
  background-color: #f2dede;
}
.table-hover > tbody > tr > td.danger:hover,
.table-hover > tbody > tr > th.danger:hover,
.table-hover > tbody > tr.danger:hover > td,
.table-hover > tbody > tr:hover > .danger,
.table-hover > tbody > tr.danger:hover > th {
  background-color: #ebcccc;
}
.table-responsive {
  overflow-x: auto;
  min-height: 0.01%;
}
@media screen and (max-width: 767px) {
  .table-responsive {
    width: 100%;
    margin-bottom: 13.5px;
    overflow-y: hidden;
    -ms-overflow-style: -ms-autohiding-scrollbar;
    border: 1px solid #ddd;
  }
  .table-responsive > .table {
    margin-bottom: 0;
  }
  .table-responsive > .table > thead > tr > th,
  .table-responsive > .table > tbody > tr > th,
  .table-responsive > .table > tfoot > tr > th,
  .table-responsive > .table > thead > tr > td,
  .table-responsive > .table > tbody > tr > td,
  .table-responsive > .table > tfoot > tr > td {
    white-space: nowrap;
  }
  .table-responsive > .table-bordered {
    border: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:first-child,
  .table-responsive > .table-bordered > tbody > tr > th:first-child,
  .table-responsive > .table-bordered > tfoot > tr > th:first-child,
  .table-responsive > .table-bordered > thead > tr > td:first-child,
  .table-responsive > .table-bordered > tbody > tr > td:first-child,
  .table-responsive > .table-bordered > tfoot > tr > td:first-child {
    border-left: 0;
  }
  .table-responsive > .table-bordered > thead > tr > th:last-child,
  .table-responsive > .table-bordered > tbody > tr > th:last-child,
  .table-responsive > .table-bordered > tfoot > tr > th:last-child,
  .table-responsive > .table-bordered > thead > tr > td:last-child,
  .table-responsive > .table-bordered > tbody > tr > td:last-child,
  .table-responsive > .table-bordered > tfoot > tr > td:last-child {
    border-right: 0;
  }
  .table-responsive > .table-bordered > tbody > tr:last-child > th,
  .table-responsive > .table-bordered > tfoot > tr:last-child > th,
  .table-responsive > .table-bordered > tbody > tr:last-child > td,
  .table-responsive > .table-bordered > tfoot > tr:last-child > td {
    border-bottom: 0;
  }
}
fieldset {
  padding: 0;
  margin: 0;
  border: 0;
  min-width: 0;
}
legend {
  display: block;
  width: 100%;
  padding: 0;
  margin-bottom: 18px;
  font-size: 19.5px;
  line-height: inherit;
  color: #333333;
  border: 0;
  border-bottom: 1px solid #e5e5e5;
}
label {
  display: inline-block;
  max-width: 100%;
  margin-bottom: 5px;
  font-weight: bold;
}
input[type="search"] {
  -webkit-box-sizing: border-box;
  -moz-box-sizing: border-box;
  box-sizing: border-box;
}
input[type="radio"],
input[type="checkbox"] {
  margin: 4px 0 0;
  margin-top: 1px \9;
  line-height: normal;
}
input[type="file"] {
  display: block;
}
input[type="range"] {
  display: block;
  width: 100%;
}
select[multiple],
select[size] {
  height: auto;
}
input[type="file"]:focus,
input[type="radio"]:focus,
input[type="checkbox"]:focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
output {
  display: block;
  padding-top: 7px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
}
.form-control {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
}
.form-control:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.form-control::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.form-control:-ms-input-placeholder {
  color: #999;
}
.form-control::-webkit-input-placeholder {
  color: #999;
}
.form-control::-ms-expand {
  border: 0;
  background-color: transparent;
}
.form-control[disabled],
.form-control[readonly],
fieldset[disabled] .form-control {
  background-color: #eeeeee;
  opacity: 1;
}
.form-control[disabled],
fieldset[disabled] .form-control {
  cursor: not-allowed;
}
textarea.form-control {
  height: auto;
}
input[type="search"] {
  -webkit-appearance: none;
}
@media screen and (-webkit-min-device-pixel-ratio: 0) {
  input[type="date"].form-control,
  input[type="time"].form-control,
  input[type="datetime-local"].form-control,
  input[type="month"].form-control {
    line-height: 32px;
  }
  input[type="date"].input-sm,
  input[type="time"].input-sm,
  input[type="datetime-local"].input-sm,
  input[type="month"].input-sm,
  .input-group-sm input[type="date"],
  .input-group-sm input[type="time"],
  .input-group-sm input[type="datetime-local"],
  .input-group-sm input[type="month"] {
    line-height: 30px;
  }
  input[type="date"].input-lg,
  input[type="time"].input-lg,
  input[type="datetime-local"].input-lg,
  input[type="month"].input-lg,
  .input-group-lg input[type="date"],
  .input-group-lg input[type="time"],
  .input-group-lg input[type="datetime-local"],
  .input-group-lg input[type="month"] {
    line-height: 45px;
  }
}
.form-group {
  margin-bottom: 15px;
}
.radio,
.checkbox {
  position: relative;
  display: block;
  margin-top: 10px;
  margin-bottom: 10px;
}
.radio label,
.checkbox label {
  min-height: 18px;
  padding-left: 20px;
  margin-bottom: 0;
  font-weight: normal;
  cursor: pointer;
}
.radio input[type="radio"],
.radio-inline input[type="radio"],
.checkbox input[type="checkbox"],
.checkbox-inline input[type="checkbox"] {
  position: absolute;
  margin-left: -20px;
  margin-top: 4px \9;
}
.radio + .radio,
.checkbox + .checkbox {
  margin-top: -5px;
}
.radio-inline,
.checkbox-inline {
  position: relative;
  display: inline-block;
  padding-left: 20px;
  margin-bottom: 0;
  vertical-align: middle;
  font-weight: normal;
  cursor: pointer;
}
.radio-inline + .radio-inline,
.checkbox-inline + .checkbox-inline {
  margin-top: 0;
  margin-left: 10px;
}
input[type="radio"][disabled],
input[type="checkbox"][disabled],
input[type="radio"].disabled,
input[type="checkbox"].disabled,
fieldset[disabled] input[type="radio"],
fieldset[disabled] input[type="checkbox"] {
  cursor: not-allowed;
}
.radio-inline.disabled,
.checkbox-inline.disabled,
fieldset[disabled] .radio-inline,
fieldset[disabled] .checkbox-inline {
  cursor: not-allowed;
}
.radio.disabled label,
.checkbox.disabled label,
fieldset[disabled] .radio label,
fieldset[disabled] .checkbox label {
  cursor: not-allowed;
}
.form-control-static {
  padding-top: 7px;
  padding-bottom: 7px;
  margin-bottom: 0;
  min-height: 31px;
}
.form-control-static.input-lg,
.form-control-static.input-sm {
  padding-left: 0;
  padding-right: 0;
}
.input-sm {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-sm {
  height: 30px;
  line-height: 30px;
}
textarea.input-sm,
select[multiple].input-sm {
  height: auto;
}
.form-group-sm .form-control {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.form-group-sm select.form-control {
  height: 30px;
  line-height: 30px;
}
.form-group-sm textarea.form-control,
.form-group-sm select[multiple].form-control {
  height: auto;
}
.form-group-sm .form-control-static {
  height: 30px;
  min-height: 30px;
  padding: 6px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.input-lg {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-lg {
  height: 45px;
  line-height: 45px;
}
textarea.input-lg,
select[multiple].input-lg {
  height: auto;
}
.form-group-lg .form-control {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.form-group-lg select.form-control {
  height: 45px;
  line-height: 45px;
}
.form-group-lg textarea.form-control,
.form-group-lg select[multiple].form-control {
  height: auto;
}
.form-group-lg .form-control-static {
  height: 45px;
  min-height: 35px;
  padding: 11px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.has-feedback {
  position: relative;
}
.has-feedback .form-control {
  padding-right: 40px;
}
.form-control-feedback {
  position: absolute;
  top: 0;
  right: 0;
  z-index: 2;
  display: block;
  width: 32px;
  height: 32px;
  line-height: 32px;
  text-align: center;
  pointer-events: none;
}
.input-lg + .form-control-feedback,
.input-group-lg + .form-control-feedback,
.form-group-lg .form-control + .form-control-feedback {
  width: 45px;
  height: 45px;
  line-height: 45px;
}
.input-sm + .form-control-feedback,
.input-group-sm + .form-control-feedback,
.form-group-sm .form-control + .form-control-feedback {
  width: 30px;
  height: 30px;
  line-height: 30px;
}
.has-success .help-block,
.has-success .control-label,
.has-success .radio,
.has-success .checkbox,
.has-success .radio-inline,
.has-success .checkbox-inline,
.has-success.radio label,
.has-success.checkbox label,
.has-success.radio-inline label,
.has-success.checkbox-inline label {
  color: #3c763d;
}
.has-success .form-control {
  border-color: #3c763d;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-success .form-control:focus {
  border-color: #2b542c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #67b168;
}
.has-success .input-group-addon {
  color: #3c763d;
  border-color: #3c763d;
  background-color: #dff0d8;
}
.has-success .form-control-feedback {
  color: #3c763d;
}
.has-warning .help-block,
.has-warning .control-label,
.has-warning .radio,
.has-warning .checkbox,
.has-warning .radio-inline,
.has-warning .checkbox-inline,
.has-warning.radio label,
.has-warning.checkbox label,
.has-warning.radio-inline label,
.has-warning.checkbox-inline label {
  color: #8a6d3b;
}
.has-warning .form-control {
  border-color: #8a6d3b;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-warning .form-control:focus {
  border-color: #66512c;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #c0a16b;
}
.has-warning .input-group-addon {
  color: #8a6d3b;
  border-color: #8a6d3b;
  background-color: #fcf8e3;
}
.has-warning .form-control-feedback {
  color: #8a6d3b;
}
.has-error .help-block,
.has-error .control-label,
.has-error .radio,
.has-error .checkbox,
.has-error .radio-inline,
.has-error .checkbox-inline,
.has-error.radio label,
.has-error.checkbox label,
.has-error.radio-inline label,
.has-error.checkbox-inline label {
  color: #a94442;
}
.has-error .form-control {
  border-color: #a94442;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
}
.has-error .form-control:focus {
  border-color: #843534;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075), 0 0 6px #ce8483;
}
.has-error .input-group-addon {
  color: #a94442;
  border-color: #a94442;
  background-color: #f2dede;
}
.has-error .form-control-feedback {
  color: #a94442;
}
.has-feedback label ~ .form-control-feedback {
  top: 23px;
}
.has-feedback label.sr-only ~ .form-control-feedback {
  top: 0;
}
.help-block {
  display: block;
  margin-top: 5px;
  margin-bottom: 10px;
  color: #404040;
}
@media (min-width: 768px) {
  .form-inline .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .form-inline .form-control-static {
    display: inline-block;
  }
  .form-inline .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .form-inline .input-group .input-group-addon,
  .form-inline .input-group .input-group-btn,
  .form-inline .input-group .form-control {
    width: auto;
  }
  .form-inline .input-group > .form-control {
    width: 100%;
  }
  .form-inline .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio,
  .form-inline .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .form-inline .radio label,
  .form-inline .checkbox label {
    padding-left: 0;
  }
  .form-inline .radio input[type="radio"],
  .form-inline .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .form-inline .has-feedback .form-control-feedback {
    top: 0;
  }
}
.form-horizontal .radio,
.form-horizontal .checkbox,
.form-horizontal .radio-inline,
.form-horizontal .checkbox-inline {
  margin-top: 0;
  margin-bottom: 0;
  padding-top: 7px;
}
.form-horizontal .radio,
.form-horizontal .checkbox {
  min-height: 25px;
}
.form-horizontal .form-group {
  margin-left: 0px;
  margin-right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .control-label {
    text-align: right;
    margin-bottom: 0;
    padding-top: 7px;
  }
}
.form-horizontal .has-feedback .form-control-feedback {
  right: 0px;
}
@media (min-width: 768px) {
  .form-horizontal .form-group-lg .control-label {
    padding-top: 11px;
    font-size: 17px;
  }
}
@media (min-width: 768px) {
  .form-horizontal .form-group-sm .control-label {
    padding-top: 6px;
    font-size: 12px;
  }
}
.btn {
  display: inline-block;
  margin-bottom: 0;
  font-weight: normal;
  text-align: center;
  vertical-align: middle;
  touch-action: manipulation;
  cursor: pointer;
  background-image: none;
  border: 1px solid transparent;
  white-space: nowrap;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  border-radius: 2px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}
.btn:focus,
.btn:active:focus,
.btn.active:focus,
.btn.focus,
.btn:active.focus,
.btn.active.focus {
  outline: 5px auto -webkit-focus-ring-color;
  outline-offset: -2px;
}
.btn:hover,
.btn:focus,
.btn.focus {
  color: #333;
  text-decoration: none;
}
.btn:active,
.btn.active {
  outline: 0;
  background-image: none;
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn.disabled,
.btn[disabled],
fieldset[disabled] .btn {
  cursor: not-allowed;
  opacity: 0.65;
  filter: alpha(opacity=65);
  -webkit-box-shadow: none;
  box-shadow: none;
}
a.btn.disabled,
fieldset[disabled] a.btn {
  pointer-events: none;
}
.btn-default {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.btn-default:focus,
.btn-default.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.btn-default:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.btn-default:active:hover,
.btn-default.active:hover,
.open > .dropdown-toggle.btn-default:hover,
.btn-default:active:focus,
.btn-default.active:focus,
.open > .dropdown-toggle.btn-default:focus,
.btn-default:active.focus,
.btn-default.active.focus,
.open > .dropdown-toggle.btn-default.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.btn-default:active,
.btn-default.active,
.open > .dropdown-toggle.btn-default {
  background-image: none;
}
.btn-default.disabled:hover,
.btn-default[disabled]:hover,
fieldset[disabled] .btn-default:hover,
.btn-default.disabled:focus,
.btn-default[disabled]:focus,
fieldset[disabled] .btn-default:focus,
.btn-default.disabled.focus,
.btn-default[disabled].focus,
fieldset[disabled] .btn-default.focus {
  background-color: #fff;
  border-color: #ccc;
}
.btn-default .badge {
  color: #fff;
  background-color: #333;
}
.btn-primary {
  color: #fff;
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary:focus,
.btn-primary.focus {
  color: #fff;
  background-color: #286090;
  border-color: #122b40;
}
.btn-primary:hover {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  color: #fff;
  background-color: #286090;
  border-color: #204d74;
}
.btn-primary:active:hover,
.btn-primary.active:hover,
.open > .dropdown-toggle.btn-primary:hover,
.btn-primary:active:focus,
.btn-primary.active:focus,
.open > .dropdown-toggle.btn-primary:focus,
.btn-primary:active.focus,
.btn-primary.active.focus,
.open > .dropdown-toggle.btn-primary.focus {
  color: #fff;
  background-color: #204d74;
  border-color: #122b40;
}
.btn-primary:active,
.btn-primary.active,
.open > .dropdown-toggle.btn-primary {
  background-image: none;
}
.btn-primary.disabled:hover,
.btn-primary[disabled]:hover,
fieldset[disabled] .btn-primary:hover,
.btn-primary.disabled:focus,
.btn-primary[disabled]:focus,
fieldset[disabled] .btn-primary:focus,
.btn-primary.disabled.focus,
.btn-primary[disabled].focus,
fieldset[disabled] .btn-primary.focus {
  background-color: #337ab7;
  border-color: #2e6da4;
}
.btn-primary .badge {
  color: #337ab7;
  background-color: #fff;
}
.btn-success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success:focus,
.btn-success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.btn-success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.btn-success:active:hover,
.btn-success.active:hover,
.open > .dropdown-toggle.btn-success:hover,
.btn-success:active:focus,
.btn-success.active:focus,
.open > .dropdown-toggle.btn-success:focus,
.btn-success:active.focus,
.btn-success.active.focus,
.open > .dropdown-toggle.btn-success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.btn-success:active,
.btn-success.active,
.open > .dropdown-toggle.btn-success {
  background-image: none;
}
.btn-success.disabled:hover,
.btn-success[disabled]:hover,
fieldset[disabled] .btn-success:hover,
.btn-success.disabled:focus,
.btn-success[disabled]:focus,
fieldset[disabled] .btn-success:focus,
.btn-success.disabled.focus,
.btn-success[disabled].focus,
fieldset[disabled] .btn-success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.btn-success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.btn-info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info:focus,
.btn-info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.btn-info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.btn-info:active:hover,
.btn-info.active:hover,
.open > .dropdown-toggle.btn-info:hover,
.btn-info:active:focus,
.btn-info.active:focus,
.open > .dropdown-toggle.btn-info:focus,
.btn-info:active.focus,
.btn-info.active.focus,
.open > .dropdown-toggle.btn-info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.btn-info:active,
.btn-info.active,
.open > .dropdown-toggle.btn-info {
  background-image: none;
}
.btn-info.disabled:hover,
.btn-info[disabled]:hover,
fieldset[disabled] .btn-info:hover,
.btn-info.disabled:focus,
.btn-info[disabled]:focus,
fieldset[disabled] .btn-info:focus,
.btn-info.disabled.focus,
.btn-info[disabled].focus,
fieldset[disabled] .btn-info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.btn-info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.btn-warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning:focus,
.btn-warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.btn-warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.btn-warning:active:hover,
.btn-warning.active:hover,
.open > .dropdown-toggle.btn-warning:hover,
.btn-warning:active:focus,
.btn-warning.active:focus,
.open > .dropdown-toggle.btn-warning:focus,
.btn-warning:active.focus,
.btn-warning.active.focus,
.open > .dropdown-toggle.btn-warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.btn-warning:active,
.btn-warning.active,
.open > .dropdown-toggle.btn-warning {
  background-image: none;
}
.btn-warning.disabled:hover,
.btn-warning[disabled]:hover,
fieldset[disabled] .btn-warning:hover,
.btn-warning.disabled:focus,
.btn-warning[disabled]:focus,
fieldset[disabled] .btn-warning:focus,
.btn-warning.disabled.focus,
.btn-warning[disabled].focus,
fieldset[disabled] .btn-warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.btn-warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.btn-danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger:focus,
.btn-danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.btn-danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.btn-danger:active:hover,
.btn-danger.active:hover,
.open > .dropdown-toggle.btn-danger:hover,
.btn-danger:active:focus,
.btn-danger.active:focus,
.open > .dropdown-toggle.btn-danger:focus,
.btn-danger:active.focus,
.btn-danger.active.focus,
.open > .dropdown-toggle.btn-danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.btn-danger:active,
.btn-danger.active,
.open > .dropdown-toggle.btn-danger {
  background-image: none;
}
.btn-danger.disabled:hover,
.btn-danger[disabled]:hover,
fieldset[disabled] .btn-danger:hover,
.btn-danger.disabled:focus,
.btn-danger[disabled]:focus,
fieldset[disabled] .btn-danger:focus,
.btn-danger.disabled.focus,
.btn-danger[disabled].focus,
fieldset[disabled] .btn-danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.btn-danger .badge {
  color: #d9534f;
  background-color: #fff;
}
.btn-link {
  color: #337ab7;
  font-weight: normal;
  border-radius: 0;
}
.btn-link,
.btn-link:active,
.btn-link.active,
.btn-link[disabled],
fieldset[disabled] .btn-link {
  background-color: transparent;
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn-link,
.btn-link:hover,
.btn-link:focus,
.btn-link:active {
  border-color: transparent;
}
.btn-link:hover,
.btn-link:focus {
  color: #23527c;
  text-decoration: underline;
  background-color: transparent;
}
.btn-link[disabled]:hover,
fieldset[disabled] .btn-link:hover,
.btn-link[disabled]:focus,
fieldset[disabled] .btn-link:focus {
  color: #777777;
  text-decoration: none;
}
.btn-lg,
.btn-group-lg > .btn {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
.btn-sm,
.btn-group-sm > .btn {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-xs,
.btn-group-xs > .btn {
  padding: 1px 5px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
.btn-block {
  display: block;
  width: 100%;
}
.btn-block + .btn-block {
  margin-top: 5px;
}
input[type="submit"].btn-block,
input[type="reset"].btn-block,
input[type="button"].btn-block {
  width: 100%;
}
.fade {
  opacity: 0;
  -webkit-transition: opacity 0.15s linear;
  -o-transition: opacity 0.15s linear;
  transition: opacity 0.15s linear;
}
.fade.in {
  opacity: 1;
}
.collapse {
  display: none;
}
.collapse.in {
  display: block;
}
tr.collapse.in {
  display: table-row;
}
tbody.collapse.in {
  display: table-row-group;
}
.collapsing {
  position: relative;
  height: 0;
  overflow: hidden;
  -webkit-transition-property: height, visibility;
  transition-property: height, visibility;
  -webkit-transition-duration: 0.35s;
  transition-duration: 0.35s;
  -webkit-transition-timing-function: ease;
  transition-timing-function: ease;
}
.caret {
  display: inline-block;
  width: 0;
  height: 0;
  margin-left: 2px;
  vertical-align: middle;
  border-top: 4px dashed;
  border-top: 4px solid \9;
  border-right: 4px solid transparent;
  border-left: 4px solid transparent;
}
.dropup,
.dropdown {
  position: relative;
}
.dropdown-toggle:focus {
  outline: 0;
}
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 1000;
  display: none;
  float: left;
  min-width: 160px;
  padding: 5px 0;
  margin: 2px 0 0;
  list-style: none;
  font-size: 13px;
  text-align: left;
  background-color: #fff;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.15);
  border-radius: 2px;
  -webkit-box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  box-shadow: 0 6px 12px rgba(0, 0, 0, 0.175);
  background-clip: padding-box;
}
.dropdown-menu.pull-right {
  right: 0;
  left: auto;
}
.dropdown-menu .divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.dropdown-menu > li > a {
  display: block;
  padding: 3px 20px;
  clear: both;
  font-weight: normal;
  line-height: 1.42857143;
  color: #333333;
  white-space: nowrap;
}
.dropdown-menu > li > a:hover,
.dropdown-menu > li > a:focus {
  text-decoration: none;
  color: #262626;
  background-color: #f5f5f5;
}
.dropdown-menu > .active > a,
.dropdown-menu > .active > a:hover,
.dropdown-menu > .active > a:focus {
  color: #fff;
  text-decoration: none;
  outline: 0;
  background-color: #337ab7;
}
.dropdown-menu > .disabled > a,
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  color: #777777;
}
.dropdown-menu > .disabled > a:hover,
.dropdown-menu > .disabled > a:focus {
  text-decoration: none;
  background-color: transparent;
  background-image: none;
  filter: progid:DXImageTransform.Microsoft.gradient(enabled = false);
  cursor: not-allowed;
}
.open > .dropdown-menu {
  display: block;
}
.open > a {
  outline: 0;
}
.dropdown-menu-right {
  left: auto;
  right: 0;
}
.dropdown-menu-left {
  left: 0;
  right: auto;
}
.dropdown-header {
  display: block;
  padding: 3px 20px;
  font-size: 12px;
  line-height: 1.42857143;
  color: #777777;
  white-space: nowrap;
}
.dropdown-backdrop {
  position: fixed;
  left: 0;
  right: 0;
  bottom: 0;
  top: 0;
  z-index: 990;
}
.pull-right > .dropdown-menu {
  right: 0;
  left: auto;
}
.dropup .caret,
.navbar-fixed-bottom .dropdown .caret {
  border-top: 0;
  border-bottom: 4px dashed;
  border-bottom: 4px solid \9;
  content: "";
}
.dropup .dropdown-menu,
.navbar-fixed-bottom .dropdown .dropdown-menu {
  top: auto;
  bottom: 100%;
  margin-bottom: 2px;
}
@media (min-width: 541px) {
  .navbar-right .dropdown-menu {
    left: auto;
    right: 0;
  }
  .navbar-right .dropdown-menu-left {
    left: 0;
    right: auto;
  }
}
.btn-group,
.btn-group-vertical {
  position: relative;
  display: inline-block;
  vertical-align: middle;
}
.btn-group > .btn,
.btn-group-vertical > .btn {
  position: relative;
  float: left;
}
.btn-group > .btn:hover,
.btn-group-vertical > .btn:hover,
.btn-group > .btn:focus,
.btn-group-vertical > .btn:focus,
.btn-group > .btn:active,
.btn-group-vertical > .btn:active,
.btn-group > .btn.active,
.btn-group-vertical > .btn.active {
  z-index: 2;
}
.btn-group .btn + .btn,
.btn-group .btn + .btn-group,
.btn-group .btn-group + .btn,
.btn-group .btn-group + .btn-group {
  margin-left: -1px;
}
.btn-toolbar {
  margin-left: -5px;
}
.btn-toolbar .btn,
.btn-toolbar .btn-group,
.btn-toolbar .input-group {
  float: left;
}
.btn-toolbar > .btn,
.btn-toolbar > .btn-group,
.btn-toolbar > .input-group {
  margin-left: 5px;
}
.btn-group > .btn:not(:first-child):not(:last-child):not(.dropdown-toggle) {
  border-radius: 0;
}
.btn-group > .btn:first-child {
  margin-left: 0;
}
.btn-group > .btn:first-child:not(:last-child):not(.dropdown-toggle) {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn:last-child:not(:first-child),
.btn-group > .dropdown-toggle:not(:first-child) {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group > .btn-group {
  float: left;
}
.btn-group > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.btn-group > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.btn-group .dropdown-toggle:active,
.btn-group.open .dropdown-toggle {
  outline: 0;
}
.btn-group > .btn + .dropdown-toggle {
  padding-left: 8px;
  padding-right: 8px;
}
.btn-group > .btn-lg + .dropdown-toggle {
  padding-left: 12px;
  padding-right: 12px;
}
.btn-group.open .dropdown-toggle {
  -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
  box-shadow: inset 0 3px 5px rgba(0, 0, 0, 0.125);
}
.btn-group.open .dropdown-toggle.btn-link {
  -webkit-box-shadow: none;
  box-shadow: none;
}
.btn .caret {
  margin-left: 0;
}
.btn-lg .caret {
  border-width: 5px 5px 0;
  border-bottom-width: 0;
}
.dropup .btn-lg .caret {
  border-width: 0 5px 5px;
}
.btn-group-vertical > .btn,
.btn-group-vertical > .btn-group,
.btn-group-vertical > .btn-group > .btn {
  display: block;
  float: none;
  width: 100%;
  max-width: 100%;
}
.btn-group-vertical > .btn-group > .btn {
  float: none;
}
.btn-group-vertical > .btn + .btn,
.btn-group-vertical > .btn + .btn-group,
.btn-group-vertical > .btn-group + .btn,
.btn-group-vertical > .btn-group + .btn-group {
  margin-top: -1px;
  margin-left: 0;
}
.btn-group-vertical > .btn:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.btn-group-vertical > .btn:first-child:not(:last-child) {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn:last-child:not(:first-child) {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
.btn-group-vertical > .btn-group:not(:first-child):not(:last-child) > .btn {
  border-radius: 0;
}
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .btn:last-child,
.btn-group-vertical > .btn-group:first-child:not(:last-child) > .dropdown-toggle {
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.btn-group-vertical > .btn-group:last-child:not(:first-child) > .btn:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.btn-group-justified {
  display: table;
  width: 100%;
  table-layout: fixed;
  border-collapse: separate;
}
.btn-group-justified > .btn,
.btn-group-justified > .btn-group {
  float: none;
  display: table-cell;
  width: 1%;
}
.btn-group-justified > .btn-group .btn {
  width: 100%;
}
.btn-group-justified > .btn-group .dropdown-menu {
  left: auto;
}
[data-toggle="buttons"] > .btn input[type="radio"],
[data-toggle="buttons"] > .btn-group > .btn input[type="radio"],
[data-toggle="buttons"] > .btn input[type="checkbox"],
[data-toggle="buttons"] > .btn-group > .btn input[type="checkbox"] {
  position: absolute;
  clip: rect(0, 0, 0, 0);
  pointer-events: none;
}
.input-group {
  position: relative;
  display: table;
  border-collapse: separate;
}
.input-group[class*="col-"] {
  float: none;
  padding-left: 0;
  padding-right: 0;
}
.input-group .form-control {
  position: relative;
  z-index: 2;
  float: left;
  width: 100%;
  margin-bottom: 0;
}
.input-group .form-control:focus {
  z-index: 3;
}
.input-group-lg > .form-control,
.input-group-lg > .input-group-addon,
.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
  border-radius: 3px;
}
select.input-group-lg > .form-control,
select.input-group-lg > .input-group-addon,
select.input-group-lg > .input-group-btn > .btn {
  height: 45px;
  line-height: 45px;
}
textarea.input-group-lg > .form-control,
textarea.input-group-lg > .input-group-addon,
textarea.input-group-lg > .input-group-btn > .btn,
select[multiple].input-group-lg > .form-control,
select[multiple].input-group-lg > .input-group-addon,
select[multiple].input-group-lg > .input-group-btn > .btn {
  height: auto;
}
.input-group-sm > .form-control,
.input-group-sm > .input-group-addon,
.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
}
select.input-group-sm > .form-control,
select.input-group-sm > .input-group-addon,
select.input-group-sm > .input-group-btn > .btn {
  height: 30px;
  line-height: 30px;
}
textarea.input-group-sm > .form-control,
textarea.input-group-sm > .input-group-addon,
textarea.input-group-sm > .input-group-btn > .btn,
select[multiple].input-group-sm > .form-control,
select[multiple].input-group-sm > .input-group-addon,
select[multiple].input-group-sm > .input-group-btn > .btn {
  height: auto;
}
.input-group-addon,
.input-group-btn,
.input-group .form-control {
  display: table-cell;
}
.input-group-addon:not(:first-child):not(:last-child),
.input-group-btn:not(:first-child):not(:last-child),
.input-group .form-control:not(:first-child):not(:last-child) {
  border-radius: 0;
}
.input-group-addon,
.input-group-btn {
  width: 1%;
  white-space: nowrap;
  vertical-align: middle;
}
.input-group-addon {
  padding: 6px 12px;
  font-size: 13px;
  font-weight: normal;
  line-height: 1;
  color: #555555;
  text-align: center;
  background-color: #eeeeee;
  border: 1px solid #ccc;
  border-radius: 2px;
}
.input-group-addon.input-sm {
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 1px;
}
.input-group-addon.input-lg {
  padding: 10px 16px;
  font-size: 17px;
  border-radius: 3px;
}
.input-group-addon input[type="radio"],
.input-group-addon input[type="checkbox"] {
  margin-top: 0;
}
.input-group .form-control:first-child,
.input-group-addon:first-child,
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group > .btn,
.input-group-btn:first-child > .dropdown-toggle,
.input-group-btn:last-child > .btn:not(:last-child):not(.dropdown-toggle),
.input-group-btn:last-child > .btn-group:not(:last-child) > .btn {
  border-bottom-right-radius: 0;
  border-top-right-radius: 0;
}
.input-group-addon:first-child {
  border-right: 0;
}
.input-group .form-control:last-child,
.input-group-addon:last-child,
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group > .btn,
.input-group-btn:last-child > .dropdown-toggle,
.input-group-btn:first-child > .btn:not(:first-child),
.input-group-btn:first-child > .btn-group:not(:first-child) > .btn {
  border-bottom-left-radius: 0;
  border-top-left-radius: 0;
}
.input-group-addon:last-child {
  border-left: 0;
}
.input-group-btn {
  position: relative;
  font-size: 0;
  white-space: nowrap;
}
.input-group-btn > .btn {
  position: relative;
}
.input-group-btn > .btn + .btn {
  margin-left: -1px;
}
.input-group-btn > .btn:hover,
.input-group-btn > .btn:focus,
.input-group-btn > .btn:active {
  z-index: 2;
}
.input-group-btn:first-child > .btn,
.input-group-btn:first-child > .btn-group {
  margin-right: -1px;
}
.input-group-btn:last-child > .btn,
.input-group-btn:last-child > .btn-group {
  z-index: 2;
  margin-left: -1px;
}
.nav {
  margin-bottom: 0;
  padding-left: 0;
  list-style: none;
}
.nav > li {
  position: relative;
  display: block;
}
.nav > li > a {
  position: relative;
  display: block;
  padding: 10px 15px;
}
.nav > li > a:hover,
.nav > li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.nav > li.disabled > a {
  color: #777777;
}
.nav > li.disabled > a:hover,
.nav > li.disabled > a:focus {
  color: #777777;
  text-decoration: none;
  background-color: transparent;
  cursor: not-allowed;
}
.nav .open > a,
.nav .open > a:hover,
.nav .open > a:focus {
  background-color: #eeeeee;
  border-color: #337ab7;
}
.nav .nav-divider {
  height: 1px;
  margin: 8px 0;
  overflow: hidden;
  background-color: #e5e5e5;
}
.nav > li > a > img {
  max-width: none;
}
.nav-tabs {
  border-bottom: 1px solid #ddd;
}
.nav-tabs > li {
  float: left;
  margin-bottom: -1px;
}
.nav-tabs > li > a {
  margin-right: 2px;
  line-height: 1.42857143;
  border: 1px solid transparent;
  border-radius: 2px 2px 0 0;
}
.nav-tabs > li > a:hover {
  border-color: #eeeeee #eeeeee #ddd;
}
.nav-tabs > li.active > a,
.nav-tabs > li.active > a:hover,
.nav-tabs > li.active > a:focus {
  color: #555555;
  background-color: #fff;
  border: 1px solid #ddd;
  border-bottom-color: transparent;
  cursor: default;
}
.nav-tabs.nav-justified {
  width: 100%;
  border-bottom: 0;
}
.nav-tabs.nav-justified > li {
  float: none;
}
.nav-tabs.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-tabs.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-tabs.nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs.nav-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs.nav-justified > .active > a,
.nav-tabs.nav-justified > .active > a:hover,
.nav-tabs.nav-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs.nav-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs.nav-justified > .active > a,
  .nav-tabs.nav-justified > .active > a:hover,
  .nav-tabs.nav-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.nav-pills > li {
  float: left;
}
.nav-pills > li > a {
  border-radius: 2px;
}
.nav-pills > li + li {
  margin-left: 2px;
}
.nav-pills > li.active > a,
.nav-pills > li.active > a:hover,
.nav-pills > li.active > a:focus {
  color: #fff;
  background-color: #337ab7;
}
.nav-stacked > li {
  float: none;
}
.nav-stacked > li + li {
  margin-top: 2px;
  margin-left: 0;
}
.nav-justified {
  width: 100%;
}
.nav-justified > li {
  float: none;
}
.nav-justified > li > a {
  text-align: center;
  margin-bottom: 5px;
}
.nav-justified > .dropdown .dropdown-menu {
  top: auto;
  left: auto;
}
@media (min-width: 768px) {
  .nav-justified > li {
    display: table-cell;
    width: 1%;
  }
  .nav-justified > li > a {
    margin-bottom: 0;
  }
}
.nav-tabs-justified {
  border-bottom: 0;
}
.nav-tabs-justified > li > a {
  margin-right: 0;
  border-radius: 2px;
}
.nav-tabs-justified > .active > a,
.nav-tabs-justified > .active > a:hover,
.nav-tabs-justified > .active > a:focus {
  border: 1px solid #ddd;
}
@media (min-width: 768px) {
  .nav-tabs-justified > li > a {
    border-bottom: 1px solid #ddd;
    border-radius: 2px 2px 0 0;
  }
  .nav-tabs-justified > .active > a,
  .nav-tabs-justified > .active > a:hover,
  .nav-tabs-justified > .active > a:focus {
    border-bottom-color: #fff;
  }
}
.tab-content > .tab-pane {
  display: none;
}
.tab-content > .active {
  display: block;
}
.nav-tabs .dropdown-menu {
  margin-top: -1px;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar {
  position: relative;
  min-height: 30px;
  margin-bottom: 18px;
  border: 1px solid transparent;
}
@media (min-width: 541px) {
  .navbar {
    border-radius: 2px;
  }
}
@media (min-width: 541px) {
  .navbar-header {
    float: left;
  }
}
.navbar-collapse {
  overflow-x: visible;
  padding-right: 0px;
  padding-left: 0px;
  border-top: 1px solid transparent;
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1);
  -webkit-overflow-scrolling: touch;
}
.navbar-collapse.in {
  overflow-y: auto;
}
@media (min-width: 541px) {
  .navbar-collapse {
    width: auto;
    border-top: 0;
    box-shadow: none;
  }
  .navbar-collapse.collapse {
    display: block !important;
    height: auto !important;
    padding-bottom: 0;
    overflow: visible !important;
  }
  .navbar-collapse.in {
    overflow-y: visible;
  }
  .navbar-fixed-top .navbar-collapse,
  .navbar-static-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    padding-left: 0;
    padding-right: 0;
  }
}
.navbar-fixed-top .navbar-collapse,
.navbar-fixed-bottom .navbar-collapse {
  max-height: 340px;
}
@media (max-device-width: 540px) and (orientation: landscape) {
  .navbar-fixed-top .navbar-collapse,
  .navbar-fixed-bottom .navbar-collapse {
    max-height: 200px;
  }
}
.container > .navbar-header,
.container-fluid > .navbar-header,
.container > .navbar-collapse,
.container-fluid > .navbar-collapse {
  margin-right: 0px;
  margin-left: 0px;
}
@media (min-width: 541px) {
  .container > .navbar-header,
  .container-fluid > .navbar-header,
  .container > .navbar-collapse,
  .container-fluid > .navbar-collapse {
    margin-right: 0;
    margin-left: 0;
  }
}
.navbar-static-top {
  z-index: 1000;
  border-width: 0 0 1px;
}
@media (min-width: 541px) {
  .navbar-static-top {
    border-radius: 0;
  }
}
.navbar-fixed-top,
.navbar-fixed-bottom {
  position: fixed;
  right: 0;
  left: 0;
  z-index: 1030;
}
@media (min-width: 541px) {
  .navbar-fixed-top,
  .navbar-fixed-bottom {
    border-radius: 0;
  }
}
.navbar-fixed-top {
  top: 0;
  border-width: 0 0 1px;
}
.navbar-fixed-bottom {
  bottom: 0;
  margin-bottom: 0;
  border-width: 1px 0 0;
}
.navbar-brand {
  float: left;
  padding: 6px 0px;
  font-size: 17px;
  line-height: 18px;
  height: 30px;
}
.navbar-brand:hover,
.navbar-brand:focus {
  text-decoration: none;
}
.navbar-brand > img {
  display: block;
}
@media (min-width: 541px) {
  .navbar > .container .navbar-brand,
  .navbar > .container-fluid .navbar-brand {
    margin-left: 0px;
  }
}
.navbar-toggle {
  position: relative;
  float: right;
  margin-right: 0px;
  padding: 9px 10px;
  margin-top: -2px;
  margin-bottom: -2px;
  background-color: transparent;
  background-image: none;
  border: 1px solid transparent;
  border-radius: 2px;
}
.navbar-toggle:focus {
  outline: 0;
}
.navbar-toggle .icon-bar {
  display: block;
  width: 22px;
  height: 2px;
  border-radius: 1px;
}
.navbar-toggle .icon-bar + .icon-bar {
  margin-top: 4px;
}
@media (min-width: 541px) {
  .navbar-toggle {
    display: none;
  }
}
.navbar-nav {
  margin: 3px 0px;
}
.navbar-nav > li > a {
  padding-top: 10px;
  padding-bottom: 10px;
  line-height: 18px;
}
@media (max-width: 540px) {
  .navbar-nav .open .dropdown-menu {
    position: static;
    float: none;
    width: auto;
    margin-top: 0;
    background-color: transparent;
    border: 0;
    box-shadow: none;
  }
  .navbar-nav .open .dropdown-menu > li > a,
  .navbar-nav .open .dropdown-menu .dropdown-header {
    padding: 5px 15px 5px 25px;
  }
  .navbar-nav .open .dropdown-menu > li > a {
    line-height: 18px;
  }
  .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-nav .open .dropdown-menu > li > a:focus {
    background-image: none;
  }
}
@media (min-width: 541px) {
  .navbar-nav {
    float: left;
    margin: 0;
  }
  .navbar-nav > li {
    float: left;
  }
  .navbar-nav > li > a {
    padding-top: 6px;
    padding-bottom: 6px;
  }
}
.navbar-form {
  margin-left: 0px;
  margin-right: 0px;
  padding: 10px 0px;
  border-top: 1px solid transparent;
  border-bottom: 1px solid transparent;
  -webkit-box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  box-shadow: inset 0 1px 0 rgba(255, 255, 255, 0.1), 0 1px 0 rgba(255, 255, 255, 0.1);
  margin-top: -1px;
  margin-bottom: -1px;
}
@media (min-width: 768px) {
  .navbar-form .form-group {
    display: inline-block;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .form-control {
    display: inline-block;
    width: auto;
    vertical-align: middle;
  }
  .navbar-form .form-control-static {
    display: inline-block;
  }
  .navbar-form .input-group {
    display: inline-table;
    vertical-align: middle;
  }
  .navbar-form .input-group .input-group-addon,
  .navbar-form .input-group .input-group-btn,
  .navbar-form .input-group .form-control {
    width: auto;
  }
  .navbar-form .input-group > .form-control {
    width: 100%;
  }
  .navbar-form .control-label {
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio,
  .navbar-form .checkbox {
    display: inline-block;
    margin-top: 0;
    margin-bottom: 0;
    vertical-align: middle;
  }
  .navbar-form .radio label,
  .navbar-form .checkbox label {
    padding-left: 0;
  }
  .navbar-form .radio input[type="radio"],
  .navbar-form .checkbox input[type="checkbox"] {
    position: relative;
    margin-left: 0;
  }
  .navbar-form .has-feedback .form-control-feedback {
    top: 0;
  }
}
@media (max-width: 540px) {
  .navbar-form .form-group {
    margin-bottom: 5px;
  }
  .navbar-form .form-group:last-child {
    margin-bottom: 0;
  }
}
@media (min-width: 541px) {
  .navbar-form {
    width: auto;
    border: 0;
    margin-left: 0;
    margin-right: 0;
    padding-top: 0;
    padding-bottom: 0;
    -webkit-box-shadow: none;
    box-shadow: none;
  }
}
.navbar-nav > li > .dropdown-menu {
  margin-top: 0;
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.navbar-fixed-bottom .navbar-nav > li > .dropdown-menu {
  margin-bottom: 0;
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
  border-bottom-right-radius: 0;
  border-bottom-left-radius: 0;
}
.navbar-btn {
  margin-top: -1px;
  margin-bottom: -1px;
}
.navbar-btn.btn-sm {
  margin-top: 0px;
  margin-bottom: 0px;
}
.navbar-btn.btn-xs {
  margin-top: 4px;
  margin-bottom: 4px;
}
.navbar-text {
  margin-top: 6px;
  margin-bottom: 6px;
}
@media (min-width: 541px) {
  .navbar-text {
    float: left;
    margin-left: 0px;
    margin-right: 0px;
  }
}
@media (min-width: 541px) {
  .navbar-left {
    float: left !important;
    float: left;
  }
  .navbar-right {
    float: right !important;
    float: right;
    margin-right: 0px;
  }
  .navbar-right ~ .navbar-right {
    margin-right: 0;
  }
}
.navbar-default {
  background-color: #f8f8f8;
  border-color: #e7e7e7;
}
.navbar-default .navbar-brand {
  color: #777;
}
.navbar-default .navbar-brand:hover,
.navbar-default .navbar-brand:focus {
  color: #5e5e5e;
  background-color: transparent;
}
.navbar-default .navbar-text {
  color: #777;
}
.navbar-default .navbar-nav > li > a {
  color: #777;
}
.navbar-default .navbar-nav > li > a:hover,
.navbar-default .navbar-nav > li > a:focus {
  color: #333;
  background-color: transparent;
}
.navbar-default .navbar-nav > .active > a,
.navbar-default .navbar-nav > .active > a:hover,
.navbar-default .navbar-nav > .active > a:focus {
  color: #555;
  background-color: #e7e7e7;
}
.navbar-default .navbar-nav > .disabled > a,
.navbar-default .navbar-nav > .disabled > a:hover,
.navbar-default .navbar-nav > .disabled > a:focus {
  color: #ccc;
  background-color: transparent;
}
.navbar-default .navbar-toggle {
  border-color: #ddd;
}
.navbar-default .navbar-toggle:hover,
.navbar-default .navbar-toggle:focus {
  background-color: #ddd;
}
.navbar-default .navbar-toggle .icon-bar {
  background-color: #888;
}
.navbar-default .navbar-collapse,
.navbar-default .navbar-form {
  border-color: #e7e7e7;
}
.navbar-default .navbar-nav > .open > a,
.navbar-default .navbar-nav > .open > a:hover,
.navbar-default .navbar-nav > .open > a:focus {
  background-color: #e7e7e7;
  color: #555;
}
@media (max-width: 540px) {
  .navbar-default .navbar-nav .open .dropdown-menu > li > a {
    color: #777;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #333;
    background-color: transparent;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #555;
    background-color: #e7e7e7;
  }
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-default .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #ccc;
    background-color: transparent;
  }
}
.navbar-default .navbar-link {
  color: #777;
}
.navbar-default .navbar-link:hover {
  color: #333;
}
.navbar-default .btn-link {
  color: #777;
}
.navbar-default .btn-link:hover,
.navbar-default .btn-link:focus {
  color: #333;
}
.navbar-default .btn-link[disabled]:hover,
fieldset[disabled] .navbar-default .btn-link:hover,
.navbar-default .btn-link[disabled]:focus,
fieldset[disabled] .navbar-default .btn-link:focus {
  color: #ccc;
}
.navbar-inverse {
  background-color: #222;
  border-color: #080808;
}
.navbar-inverse .navbar-brand {
  color: #9d9d9d;
}
.navbar-inverse .navbar-brand:hover,
.navbar-inverse .navbar-brand:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-text {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a {
  color: #9d9d9d;
}
.navbar-inverse .navbar-nav > li > a:hover,
.navbar-inverse .navbar-nav > li > a:focus {
  color: #fff;
  background-color: transparent;
}
.navbar-inverse .navbar-nav > .active > a,
.navbar-inverse .navbar-nav > .active > a:hover,
.navbar-inverse .navbar-nav > .active > a:focus {
  color: #fff;
  background-color: #080808;
}
.navbar-inverse .navbar-nav > .disabled > a,
.navbar-inverse .navbar-nav > .disabled > a:hover,
.navbar-inverse .navbar-nav > .disabled > a:focus {
  color: #444;
  background-color: transparent;
}
.navbar-inverse .navbar-toggle {
  border-color: #333;
}
.navbar-inverse .navbar-toggle:hover,
.navbar-inverse .navbar-toggle:focus {
  background-color: #333;
}
.navbar-inverse .navbar-toggle .icon-bar {
  background-color: #fff;
}
.navbar-inverse .navbar-collapse,
.navbar-inverse .navbar-form {
  border-color: #101010;
}
.navbar-inverse .navbar-nav > .open > a,
.navbar-inverse .navbar-nav > .open > a:hover,
.navbar-inverse .navbar-nav > .open > a:focus {
  background-color: #080808;
  color: #fff;
}
@media (max-width: 540px) {
  .navbar-inverse .navbar-nav .open .dropdown-menu > .dropdown-header {
    border-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu .divider {
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a {
    color: #9d9d9d;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > li > a:focus {
    color: #fff;
    background-color: transparent;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .active > a:focus {
    color: #fff;
    background-color: #080808;
  }
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:hover,
  .navbar-inverse .navbar-nav .open .dropdown-menu > .disabled > a:focus {
    color: #444;
    background-color: transparent;
  }
}
.navbar-inverse .navbar-link {
  color: #9d9d9d;
}
.navbar-inverse .navbar-link:hover {
  color: #fff;
}
.navbar-inverse .btn-link {
  color: #9d9d9d;
}
.navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link:focus {
  color: #fff;
}
.navbar-inverse .btn-link[disabled]:hover,
fieldset[disabled] .navbar-inverse .btn-link:hover,
.navbar-inverse .btn-link[disabled]:focus,
fieldset[disabled] .navbar-inverse .btn-link:focus {
  color: #444;
}
.breadcrumb {
  padding: 8px 15px;
  margin-bottom: 18px;
  list-style: none;
  background-color: #f5f5f5;
  border-radius: 2px;
}
.breadcrumb > li {
  display: inline-block;
}
.breadcrumb > li + li:before {
  content: "/\00a0";
  padding: 0 5px;
  color: #5e5e5e;
}
.breadcrumb > .active {
  color: #777777;
}
.pagination {
  display: inline-block;
  padding-left: 0;
  margin: 18px 0;
  border-radius: 2px;
}
.pagination > li {
  display: inline;
}
.pagination > li > a,
.pagination > li > span {
  position: relative;
  float: left;
  padding: 6px 12px;
  line-height: 1.42857143;
  text-decoration: none;
  color: #337ab7;
  background-color: #fff;
  border: 1px solid #ddd;
  margin-left: -1px;
}
.pagination > li:first-child > a,
.pagination > li:first-child > span {
  margin-left: 0;
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.pagination > li:last-child > a,
.pagination > li:last-child > span {
  border-bottom-right-radius: 2px;
  border-top-right-radius: 2px;
}
.pagination > li > a:hover,
.pagination > li > span:hover,
.pagination > li > a:focus,
.pagination > li > span:focus {
  z-index: 2;
  color: #23527c;
  background-color: #eeeeee;
  border-color: #ddd;
}
.pagination > .active > a,
.pagination > .active > span,
.pagination > .active > a:hover,
.pagination > .active > span:hover,
.pagination > .active > a:focus,
.pagination > .active > span:focus {
  z-index: 3;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
  cursor: default;
}
.pagination > .disabled > span,
.pagination > .disabled > span:hover,
.pagination > .disabled > span:focus,
.pagination > .disabled > a,
.pagination > .disabled > a:hover,
.pagination > .disabled > a:focus {
  color: #777777;
  background-color: #fff;
  border-color: #ddd;
  cursor: not-allowed;
}
.pagination-lg > li > a,
.pagination-lg > li > span {
  padding: 10px 16px;
  font-size: 17px;
  line-height: 1.3333333;
}
.pagination-lg > li:first-child > a,
.pagination-lg > li:first-child > span {
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px;
}
.pagination-lg > li:last-child > a,
.pagination-lg > li:last-child > span {
  border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
}
.pagination-sm > li > a,
.pagination-sm > li > span {
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
}
.pagination-sm > li:first-child > a,
.pagination-sm > li:first-child > span {
  border-bottom-left-radius: 1px;
  border-top-left-radius: 1px;
}
.pagination-sm > li:last-child > a,
.pagination-sm > li:last-child > span {
  border-bottom-right-radius: 1px;
  border-top-right-radius: 1px;
}
.pager {
  padding-left: 0;
  margin: 18px 0;
  list-style: none;
  text-align: center;
}
.pager li {
  display: inline;
}
.pager li > a,
.pager li > span {
  display: inline-block;
  padding: 5px 14px;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 15px;
}
.pager li > a:hover,
.pager li > a:focus {
  text-decoration: none;
  background-color: #eeeeee;
}
.pager .next > a,
.pager .next > span {
  float: right;
}
.pager .previous > a,
.pager .previous > span {
  float: left;
}
.pager .disabled > a,
.pager .disabled > a:hover,
.pager .disabled > a:focus,
.pager .disabled > span {
  color: #777777;
  background-color: #fff;
  cursor: not-allowed;
}
.label {
  display: inline;
  padding: .2em .6em .3em;
  font-size: 75%;
  font-weight: bold;
  line-height: 1;
  color: #fff;
  text-align: center;
  white-space: nowrap;
  vertical-align: baseline;
  border-radius: .25em;
}
a.label:hover,
a.label:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.label:empty {
  display: none;
}
.btn .label {
  position: relative;
  top: -1px;
}
.label-default {
  background-color: #777777;
}
.label-default[href]:hover,
.label-default[href]:focus {
  background-color: #5e5e5e;
}
.label-primary {
  background-color: #337ab7;
}
.label-primary[href]:hover,
.label-primary[href]:focus {
  background-color: #286090;
}
.label-success {
  background-color: #5cb85c;
}
.label-success[href]:hover,
.label-success[href]:focus {
  background-color: #449d44;
}
.label-info {
  background-color: #5bc0de;
}
.label-info[href]:hover,
.label-info[href]:focus {
  background-color: #31b0d5;
}
.label-warning {
  background-color: #f0ad4e;
}
.label-warning[href]:hover,
.label-warning[href]:focus {
  background-color: #ec971f;
}
.label-danger {
  background-color: #d9534f;
}
.label-danger[href]:hover,
.label-danger[href]:focus {
  background-color: #c9302c;
}
.badge {
  display: inline-block;
  min-width: 10px;
  padding: 3px 7px;
  font-size: 12px;
  font-weight: bold;
  color: #fff;
  line-height: 1;
  vertical-align: middle;
  white-space: nowrap;
  text-align: center;
  background-color: #777777;
  border-radius: 10px;
}
.badge:empty {
  display: none;
}
.btn .badge {
  position: relative;
  top: -1px;
}
.btn-xs .badge,
.btn-group-xs > .btn .badge {
  top: 0;
  padding: 1px 5px;
}
a.badge:hover,
a.badge:focus {
  color: #fff;
  text-decoration: none;
  cursor: pointer;
}
.list-group-item.active > .badge,
.nav-pills > .active > a > .badge {
  color: #337ab7;
  background-color: #fff;
}
.list-group-item > .badge {
  float: right;
}
.list-group-item > .badge + .badge {
  margin-right: 5px;
}
.nav-pills > li > a > .badge {
  margin-left: 3px;
}
.jumbotron {
  padding-top: 30px;
  padding-bottom: 30px;
  margin-bottom: 30px;
  color: inherit;
  background-color: #eeeeee;
}
.jumbotron h1,
.jumbotron .h1 {
  color: inherit;
}
.jumbotron p {
  margin-bottom: 15px;
  font-size: 20px;
  font-weight: 200;
}
.jumbotron > hr {
  border-top-color: #d5d5d5;
}
.container .jumbotron,
.container-fluid .jumbotron {
  border-radius: 3px;
  padding-left: 0px;
  padding-right: 0px;
}
.jumbotron .container {
  max-width: 100%;
}
@media screen and (min-width: 768px) {
  .jumbotron {
    padding-top: 48px;
    padding-bottom: 48px;
  }
  .container .jumbotron,
  .container-fluid .jumbotron {
    padding-left: 60px;
    padding-right: 60px;
  }
  .jumbotron h1,
  .jumbotron .h1 {
    font-size: 59px;
  }
}
.thumbnail {
  display: block;
  padding: 4px;
  margin-bottom: 18px;
  line-height: 1.42857143;
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 2px;
  -webkit-transition: border 0.2s ease-in-out;
  -o-transition: border 0.2s ease-in-out;
  transition: border 0.2s ease-in-out;
}
.thumbnail > img,
.thumbnail a > img {
  margin-left: auto;
  margin-right: auto;
}
a.thumbnail:hover,
a.thumbnail:focus,
a.thumbnail.active {
  border-color: #337ab7;
}
.thumbnail .caption {
  padding: 9px;
  color: #000;
}
.alert {
  padding: 15px;
  margin-bottom: 18px;
  border: 1px solid transparent;
  border-radius: 2px;
}
.alert h4 {
  margin-top: 0;
  color: inherit;
}
.alert .alert-link {
  font-weight: bold;
}
.alert > p,
.alert > ul {
  margin-bottom: 0;
}
.alert > p + p {
  margin-top: 5px;
}
.alert-dismissable,
.alert-dismissible {
  padding-right: 35px;
}
.alert-dismissable .close,
.alert-dismissible .close {
  position: relative;
  top: -2px;
  right: -21px;
  color: inherit;
}
.alert-success {
  background-color: #dff0d8;
  border-color: #d6e9c6;
  color: #3c763d;
}
.alert-success hr {
  border-top-color: #c9e2b3;
}
.alert-success .alert-link {
  color: #2b542c;
}
.alert-info {
  background-color: #d9edf7;
  border-color: #bce8f1;
  color: #31708f;
}
.alert-info hr {
  border-top-color: #a6e1ec;
}
.alert-info .alert-link {
  color: #245269;
}
.alert-warning {
  background-color: #fcf8e3;
  border-color: #faebcc;
  color: #8a6d3b;
}
.alert-warning hr {
  border-top-color: #f7e1b5;
}
.alert-warning .alert-link {
  color: #66512c;
}
.alert-danger {
  background-color: #f2dede;
  border-color: #ebccd1;
  color: #a94442;
}
.alert-danger hr {
  border-top-color: #e4b9c0;
}
.alert-danger .alert-link {
  color: #843534;
}
@-webkit-keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
@keyframes progress-bar-stripes {
  from {
    background-position: 40px 0;
  }
  to {
    background-position: 0 0;
  }
}
.progress {
  overflow: hidden;
  height: 18px;
  margin-bottom: 18px;
  background-color: #f5f5f5;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
}
.progress-bar {
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 18px;
  color: #fff;
  text-align: center;
  background-color: #337ab7;
  -webkit-box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.15);
  -webkit-transition: width 0.6s ease;
  -o-transition: width 0.6s ease;
  transition: width 0.6s ease;
}
.progress-striped .progress-bar,
.progress-bar-striped {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-size: 40px 40px;
}
.progress.active .progress-bar,
.progress-bar.active {
  -webkit-animation: progress-bar-stripes 2s linear infinite;
  -o-animation: progress-bar-stripes 2s linear infinite;
  animation: progress-bar-stripes 2s linear infinite;
}
.progress-bar-success {
  background-color: #5cb85c;
}
.progress-striped .progress-bar-success {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-info {
  background-color: #5bc0de;
}
.progress-striped .progress-bar-info {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-warning {
  background-color: #f0ad4e;
}
.progress-striped .progress-bar-warning {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.progress-bar-danger {
  background-color: #d9534f;
}
.progress-striped .progress-bar-danger {
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.15) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.15) 50%, rgba(255, 255, 255, 0.15) 75%, transparent 75%, transparent);
}
.media {
  margin-top: 15px;
}
.media:first-child {
  margin-top: 0;
}
.media,
.media-body {
  zoom: 1;
  overflow: hidden;
}
.media-body {
  width: 10000px;
}
.media-object {
  display: block;
}
.media-object.img-thumbnail {
  max-width: none;
}
.media-right,
.media > .pull-right {
  padding-left: 10px;
}
.media-left,
.media > .pull-left {
  padding-right: 10px;
}
.media-left,
.media-right,
.media-body {
  display: table-cell;
  vertical-align: top;
}
.media-middle {
  vertical-align: middle;
}
.media-bottom {
  vertical-align: bottom;
}
.media-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.media-list {
  padding-left: 0;
  list-style: none;
}
.list-group {
  margin-bottom: 20px;
  padding-left: 0;
}
.list-group-item {
  position: relative;
  display: block;
  padding: 10px 15px;
  margin-bottom: -1px;
  background-color: #fff;
  border: 1px solid #ddd;
}
.list-group-item:first-child {
  border-top-right-radius: 2px;
  border-top-left-radius: 2px;
}
.list-group-item:last-child {
  margin-bottom: 0;
  border-bottom-right-radius: 2px;
  border-bottom-left-radius: 2px;
}
a.list-group-item,
button.list-group-item {
  color: #555;
}
a.list-group-item .list-group-item-heading,
button.list-group-item .list-group-item-heading {
  color: #333;
}
a.list-group-item:hover,
button.list-group-item:hover,
a.list-group-item:focus,
button.list-group-item:focus {
  text-decoration: none;
  color: #555;
  background-color: #f5f5f5;
}
button.list-group-item {
  width: 100%;
  text-align: left;
}
.list-group-item.disabled,
.list-group-item.disabled:hover,
.list-group-item.disabled:focus {
  background-color: #eeeeee;
  color: #777777;
  cursor: not-allowed;
}
.list-group-item.disabled .list-group-item-heading,
.list-group-item.disabled:hover .list-group-item-heading,
.list-group-item.disabled:focus .list-group-item-heading {
  color: inherit;
}
.list-group-item.disabled .list-group-item-text,
.list-group-item.disabled:hover .list-group-item-text,
.list-group-item.disabled:focus .list-group-item-text {
  color: #777777;
}
.list-group-item.active,
.list-group-item.active:hover,
.list-group-item.active:focus {
  z-index: 2;
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.list-group-item.active .list-group-item-heading,
.list-group-item.active:hover .list-group-item-heading,
.list-group-item.active:focus .list-group-item-heading,
.list-group-item.active .list-group-item-heading > small,
.list-group-item.active:hover .list-group-item-heading > small,
.list-group-item.active:focus .list-group-item-heading > small,
.list-group-item.active .list-group-item-heading > .small,
.list-group-item.active:hover .list-group-item-heading > .small,
.list-group-item.active:focus .list-group-item-heading > .small {
  color: inherit;
}
.list-group-item.active .list-group-item-text,
.list-group-item.active:hover .list-group-item-text,
.list-group-item.active:focus .list-group-item-text {
  color: #c7ddef;
}
.list-group-item-success {
  color: #3c763d;
  background-color: #dff0d8;
}
a.list-group-item-success,
button.list-group-item-success {
  color: #3c763d;
}
a.list-group-item-success .list-group-item-heading,
button.list-group-item-success .list-group-item-heading {
  color: inherit;
}
a.list-group-item-success:hover,
button.list-group-item-success:hover,
a.list-group-item-success:focus,
button.list-group-item-success:focus {
  color: #3c763d;
  background-color: #d0e9c6;
}
a.list-group-item-success.active,
button.list-group-item-success.active,
a.list-group-item-success.active:hover,
button.list-group-item-success.active:hover,
a.list-group-item-success.active:focus,
button.list-group-item-success.active:focus {
  color: #fff;
  background-color: #3c763d;
  border-color: #3c763d;
}
.list-group-item-info {
  color: #31708f;
  background-color: #d9edf7;
}
a.list-group-item-info,
button.list-group-item-info {
  color: #31708f;
}
a.list-group-item-info .list-group-item-heading,
button.list-group-item-info .list-group-item-heading {
  color: inherit;
}
a.list-group-item-info:hover,
button.list-group-item-info:hover,
a.list-group-item-info:focus,
button.list-group-item-info:focus {
  color: #31708f;
  background-color: #c4e3f3;
}
a.list-group-item-info.active,
button.list-group-item-info.active,
a.list-group-item-info.active:hover,
button.list-group-item-info.active:hover,
a.list-group-item-info.active:focus,
button.list-group-item-info.active:focus {
  color: #fff;
  background-color: #31708f;
  border-color: #31708f;
}
.list-group-item-warning {
  color: #8a6d3b;
  background-color: #fcf8e3;
}
a.list-group-item-warning,
button.list-group-item-warning {
  color: #8a6d3b;
}
a.list-group-item-warning .list-group-item-heading,
button.list-group-item-warning .list-group-item-heading {
  color: inherit;
}
a.list-group-item-warning:hover,
button.list-group-item-warning:hover,
a.list-group-item-warning:focus,
button.list-group-item-warning:focus {
  color: #8a6d3b;
  background-color: #faf2cc;
}
a.list-group-item-warning.active,
button.list-group-item-warning.active,
a.list-group-item-warning.active:hover,
button.list-group-item-warning.active:hover,
a.list-group-item-warning.active:focus,
button.list-group-item-warning.active:focus {
  color: #fff;
  background-color: #8a6d3b;
  border-color: #8a6d3b;
}
.list-group-item-danger {
  color: #a94442;
  background-color: #f2dede;
}
a.list-group-item-danger,
button.list-group-item-danger {
  color: #a94442;
}
a.list-group-item-danger .list-group-item-heading,
button.list-group-item-danger .list-group-item-heading {
  color: inherit;
}
a.list-group-item-danger:hover,
button.list-group-item-danger:hover,
a.list-group-item-danger:focus,
button.list-group-item-danger:focus {
  color: #a94442;
  background-color: #ebcccc;
}
a.list-group-item-danger.active,
button.list-group-item-danger.active,
a.list-group-item-danger.active:hover,
button.list-group-item-danger.active:hover,
a.list-group-item-danger.active:focus,
button.list-group-item-danger.active:focus {
  color: #fff;
  background-color: #a94442;
  border-color: #a94442;
}
.list-group-item-heading {
  margin-top: 0;
  margin-bottom: 5px;
}
.list-group-item-text {
  margin-bottom: 0;
  line-height: 1.3;
}
.panel {
  margin-bottom: 18px;
  background-color: #fff;
  border: 1px solid transparent;
  border-radius: 2px;
  -webkit-box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: 0 1px 1px rgba(0, 0, 0, 0.05);
}
.panel-body {
  padding: 15px;
}
.panel-heading {
  padding: 10px 15px;
  border-bottom: 1px solid transparent;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel-heading > .dropdown .dropdown-toggle {
  color: inherit;
}
.panel-title {
  margin-top: 0;
  margin-bottom: 0;
  font-size: 15px;
  color: inherit;
}
.panel-title > a,
.panel-title > small,
.panel-title > .small,
.panel-title > small > a,
.panel-title > .small > a {
  color: inherit;
}
.panel-footer {
  padding: 10px 15px;
  background-color: #f5f5f5;
  border-top: 1px solid #ddd;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .list-group,
.panel > .panel-collapse > .list-group {
  margin-bottom: 0;
}
.panel > .list-group .list-group-item,
.panel > .panel-collapse > .list-group .list-group-item {
  border-width: 1px 0;
  border-radius: 0;
}
.panel > .list-group:first-child .list-group-item:first-child,
.panel > .panel-collapse > .list-group:first-child .list-group-item:first-child {
  border-top: 0;
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .list-group:last-child .list-group-item:last-child,
.panel > .panel-collapse > .list-group:last-child .list-group-item:last-child {
  border-bottom: 0;
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .panel-heading + .panel-collapse > .list-group .list-group-item:first-child {
  border-top-right-radius: 0;
  border-top-left-radius: 0;
}
.panel-heading + .list-group .list-group-item:first-child {
  border-top-width: 0;
}
.list-group + .panel-footer {
  border-top-width: 0;
}
.panel > .table,
.panel > .table-responsive > .table,
.panel > .panel-collapse > .table {
  margin-bottom: 0;
}
.panel > .table caption,
.panel > .table-responsive > .table caption,
.panel > .panel-collapse > .table caption {
  padding-left: 15px;
  padding-right: 15px;
}
.panel > .table:first-child,
.panel > .table-responsive:first-child > .table:first-child {
  border-top-right-radius: 1px;
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child {
  border-top-left-radius: 1px;
  border-top-right-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:first-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:first-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:first-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:first-child {
  border-top-left-radius: 1px;
}
.panel > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child td:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child td:last-child,
.panel > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > thead:first-child > tr:first-child th:last-child,
.panel > .table:first-child > tbody:first-child > tr:first-child th:last-child,
.panel > .table-responsive:first-child > .table:first-child > tbody:first-child > tr:first-child th:last-child {
  border-top-right-radius: 1px;
}
.panel > .table:last-child,
.panel > .table-responsive:last-child > .table:last-child {
  border-bottom-right-radius: 1px;
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child {
  border-bottom-left-radius: 1px;
  border-bottom-right-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:first-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:first-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:first-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:first-child {
  border-bottom-left-radius: 1px;
}
.panel > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child td:last-child,
.panel > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tbody:last-child > tr:last-child th:last-child,
.panel > .table:last-child > tfoot:last-child > tr:last-child th:last-child,
.panel > .table-responsive:last-child > .table:last-child > tfoot:last-child > tr:last-child th:last-child {
  border-bottom-right-radius: 1px;
}
.panel > .panel-body + .table,
.panel > .panel-body + .table-responsive,
.panel > .table + .panel-body,
.panel > .table-responsive + .panel-body {
  border-top: 1px solid #ddd;
}
.panel > .table > tbody:first-child > tr:first-child th,
.panel > .table > tbody:first-child > tr:first-child td {
  border-top: 0;
}
.panel > .table-bordered,
.panel > .table-responsive > .table-bordered {
  border: 0;
}
.panel > .table-bordered > thead > tr > th:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:first-child,
.panel > .table-bordered > tbody > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:first-child,
.panel > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:first-child,
.panel > .table-bordered > thead > tr > td:first-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:first-child,
.panel > .table-bordered > tbody > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:first-child,
.panel > .table-bordered > tfoot > tr > td:first-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:first-child {
  border-left: 0;
}
.panel > .table-bordered > thead > tr > th:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > th:last-child,
.panel > .table-bordered > tbody > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > th:last-child,
.panel > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > th:last-child,
.panel > .table-bordered > thead > tr > td:last-child,
.panel > .table-responsive > .table-bordered > thead > tr > td:last-child,
.panel > .table-bordered > tbody > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tbody > tr > td:last-child,
.panel > .table-bordered > tfoot > tr > td:last-child,
.panel > .table-responsive > .table-bordered > tfoot > tr > td:last-child {
  border-right: 0;
}
.panel > .table-bordered > thead > tr:first-child > td,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > td,
.panel > .table-bordered > tbody > tr:first-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > td,
.panel > .table-bordered > thead > tr:first-child > th,
.panel > .table-responsive > .table-bordered > thead > tr:first-child > th,
.panel > .table-bordered > tbody > tr:first-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:first-child > th {
  border-bottom: 0;
}
.panel > .table-bordered > tbody > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > td,
.panel > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > td,
.panel > .table-bordered > tbody > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tbody > tr:last-child > th,
.panel > .table-bordered > tfoot > tr:last-child > th,
.panel > .table-responsive > .table-bordered > tfoot > tr:last-child > th {
  border-bottom: 0;
}
.panel > .table-responsive {
  border: 0;
  margin-bottom: 0;
}
.panel-group {
  margin-bottom: 18px;
}
.panel-group .panel {
  margin-bottom: 0;
  border-radius: 2px;
}
.panel-group .panel + .panel {
  margin-top: 5px;
}
.panel-group .panel-heading {
  border-bottom: 0;
}
.panel-group .panel-heading + .panel-collapse > .panel-body,
.panel-group .panel-heading + .panel-collapse > .list-group {
  border-top: 1px solid #ddd;
}
.panel-group .panel-footer {
  border-top: 0;
}
.panel-group .panel-footer + .panel-collapse .panel-body {
  border-bottom: 1px solid #ddd;
}
.panel-default {
  border-color: #ddd;
}
.panel-default > .panel-heading {
  color: #333333;
  background-color: #f5f5f5;
  border-color: #ddd;
}
.panel-default > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ddd;
}
.panel-default > .panel-heading .badge {
  color: #f5f5f5;
  background-color: #333333;
}
.panel-default > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ddd;
}
.panel-primary {
  border-color: #337ab7;
}
.panel-primary > .panel-heading {
  color: #fff;
  background-color: #337ab7;
  border-color: #337ab7;
}
.panel-primary > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #337ab7;
}
.panel-primary > .panel-heading .badge {
  color: #337ab7;
  background-color: #fff;
}
.panel-primary > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #337ab7;
}
.panel-success {
  border-color: #d6e9c6;
}
.panel-success > .panel-heading {
  color: #3c763d;
  background-color: #dff0d8;
  border-color: #d6e9c6;
}
.panel-success > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #d6e9c6;
}
.panel-success > .panel-heading .badge {
  color: #dff0d8;
  background-color: #3c763d;
}
.panel-success > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #d6e9c6;
}
.panel-info {
  border-color: #bce8f1;
}
.panel-info > .panel-heading {
  color: #31708f;
  background-color: #d9edf7;
  border-color: #bce8f1;
}
.panel-info > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #bce8f1;
}
.panel-info > .panel-heading .badge {
  color: #d9edf7;
  background-color: #31708f;
}
.panel-info > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #bce8f1;
}
.panel-warning {
  border-color: #faebcc;
}
.panel-warning > .panel-heading {
  color: #8a6d3b;
  background-color: #fcf8e3;
  border-color: #faebcc;
}
.panel-warning > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #faebcc;
}
.panel-warning > .panel-heading .badge {
  color: #fcf8e3;
  background-color: #8a6d3b;
}
.panel-warning > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #faebcc;
}
.panel-danger {
  border-color: #ebccd1;
}
.panel-danger > .panel-heading {
  color: #a94442;
  background-color: #f2dede;
  border-color: #ebccd1;
}
.panel-danger > .panel-heading + .panel-collapse > .panel-body {
  border-top-color: #ebccd1;
}
.panel-danger > .panel-heading .badge {
  color: #f2dede;
  background-color: #a94442;
}
.panel-danger > .panel-footer + .panel-collapse > .panel-body {
  border-bottom-color: #ebccd1;
}
.embed-responsive {
  position: relative;
  display: block;
  height: 0;
  padding: 0;
  overflow: hidden;
}
.embed-responsive .embed-responsive-item,
.embed-responsive iframe,
.embed-responsive embed,
.embed-responsive object,
.embed-responsive video {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  height: 100%;
  width: 100%;
  border: 0;
}
.embed-responsive-16by9 {
  padding-bottom: 56.25%;
}
.embed-responsive-4by3 {
  padding-bottom: 75%;
}
.well {
  min-height: 20px;
  padding: 19px;
  margin-bottom: 20px;
  background-color: #f5f5f5;
  border: 1px solid #e3e3e3;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.05);
}
.well blockquote {
  border-color: #ddd;
  border-color: rgba(0, 0, 0, 0.15);
}
.well-lg {
  padding: 24px;
  border-radius: 3px;
}
.well-sm {
  padding: 9px;
  border-radius: 1px;
}
.close {
  float: right;
  font-size: 19.5px;
  font-weight: bold;
  line-height: 1;
  color: #000;
  text-shadow: 0 1px 0 #fff;
  opacity: 0.2;
  filter: alpha(opacity=20);
}
.close:hover,
.close:focus {
  color: #000;
  text-decoration: none;
  cursor: pointer;
  opacity: 0.5;
  filter: alpha(opacity=50);
}
button.close {
  padding: 0;
  cursor: pointer;
  background: transparent;
  border: 0;
  -webkit-appearance: none;
}
.modal-open {
  overflow: hidden;
}
.modal {
  display: none;
  overflow: hidden;
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1050;
  -webkit-overflow-scrolling: touch;
  outline: 0;
}
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, -25%);
  -ms-transform: translate(0, -25%);
  -o-transform: translate(0, -25%);
  transform: translate(0, -25%);
  -webkit-transition: -webkit-transform 0.3s ease-out;
  -moz-transition: -moz-transform 0.3s ease-out;
  -o-transition: -o-transform 0.3s ease-out;
  transition: transform 0.3s ease-out;
}
.modal.in .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
.modal-open .modal {
  overflow-x: hidden;
  overflow-y: auto;
}
.modal-dialog {
  position: relative;
  width: auto;
  margin: 10px;
}
.modal-content {
  position: relative;
  background-color: #fff;
  border: 1px solid #999;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  box-shadow: 0 3px 9px rgba(0, 0, 0, 0.5);
  background-clip: padding-box;
  outline: 0;
}
.modal-backdrop {
  position: fixed;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  z-index: 1040;
  background-color: #000;
}
.modal-backdrop.fade {
  opacity: 0;
  filter: alpha(opacity=0);
}
.modal-backdrop.in {
  opacity: 0.5;
  filter: alpha(opacity=50);
}
.modal-header {
  padding: 15px;
  border-bottom: 1px solid #e5e5e5;
}
.modal-header .close {
  margin-top: -2px;
}
.modal-title {
  margin: 0;
  line-height: 1.42857143;
}
.modal-body {
  position: relative;
  padding: 15px;
}
.modal-footer {
  padding: 15px;
  text-align: right;
  border-top: 1px solid #e5e5e5;
}
.modal-footer .btn + .btn {
  margin-left: 5px;
  margin-bottom: 0;
}
.modal-footer .btn-group .btn + .btn {
  margin-left: -1px;
}
.modal-footer .btn-block + .btn-block {
  margin-left: 0;
}
.modal-scrollbar-measure {
  position: absolute;
  top: -9999px;
  width: 50px;
  height: 50px;
  overflow: scroll;
}
@media (min-width: 768px) {
  .modal-dialog {
    width: 600px;
    margin: 30px auto;
  }
  .modal-content {
    -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.5);
  }
  .modal-sm {
    width: 300px;
  }
}
@media (min-width: 992px) {
  .modal-lg {
    width: 900px;
  }
}
.tooltip {
  position: absolute;
  z-index: 1070;
  display: block;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 12px;
  opacity: 0;
  filter: alpha(opacity=0);
}
.tooltip.in {
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.tooltip.top {
  margin-top: -3px;
  padding: 5px 0;
}
.tooltip.right {
  margin-left: 3px;
  padding: 0 5px;
}
.tooltip.bottom {
  margin-top: 3px;
  padding: 5px 0;
}
.tooltip.left {
  margin-left: -3px;
  padding: 0 5px;
}
.tooltip-inner {
  max-width: 200px;
  padding: 3px 8px;
  color: #fff;
  text-align: center;
  background-color: #000;
  border-radius: 2px;
}
.tooltip-arrow {
  position: absolute;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.tooltip.top .tooltip-arrow {
  bottom: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-left .tooltip-arrow {
  bottom: 0;
  right: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.top-right .tooltip-arrow {
  bottom: 0;
  left: 5px;
  margin-bottom: -5px;
  border-width: 5px 5px 0;
  border-top-color: #000;
}
.tooltip.right .tooltip-arrow {
  top: 50%;
  left: 0;
  margin-top: -5px;
  border-width: 5px 5px 5px 0;
  border-right-color: #000;
}
.tooltip.left .tooltip-arrow {
  top: 50%;
  right: 0;
  margin-top: -5px;
  border-width: 5px 0 5px 5px;
  border-left-color: #000;
}
.tooltip.bottom .tooltip-arrow {
  top: 0;
  left: 50%;
  margin-left: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-left .tooltip-arrow {
  top: 0;
  right: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.tooltip.bottom-right .tooltip-arrow {
  top: 0;
  left: 5px;
  margin-top: -5px;
  border-width: 0 5px 5px;
  border-bottom-color: #000;
}
.popover {
  position: absolute;
  top: 0;
  left: 0;
  z-index: 1060;
  display: none;
  max-width: 276px;
  padding: 1px;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-style: normal;
  font-weight: normal;
  letter-spacing: normal;
  line-break: auto;
  line-height: 1.42857143;
  text-align: left;
  text-align: start;
  text-decoration: none;
  text-shadow: none;
  text-transform: none;
  white-space: normal;
  word-break: normal;
  word-spacing: normal;
  word-wrap: normal;
  font-size: 13px;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ccc;
  border: 1px solid rgba(0, 0, 0, 0.2);
  border-radius: 3px;
  -webkit-box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
  box-shadow: 0 5px 10px rgba(0, 0, 0, 0.2);
}
.popover.top {
  margin-top: -10px;
}
.popover.right {
  margin-left: 10px;
}
.popover.bottom {
  margin-top: 10px;
}
.popover.left {
  margin-left: -10px;
}
.popover-title {
  margin: 0;
  padding: 8px 14px;
  font-size: 13px;
  background-color: #f7f7f7;
  border-bottom: 1px solid #ebebeb;
  border-radius: 2px 2px 0 0;
}
.popover-content {
  padding: 9px 14px;
}
.popover > .arrow,
.popover > .arrow:after {
  position: absolute;
  display: block;
  width: 0;
  height: 0;
  border-color: transparent;
  border-style: solid;
}
.popover > .arrow {
  border-width: 11px;
}
.popover > .arrow:after {
  border-width: 10px;
  content: "";
}
.popover.top > .arrow {
  left: 50%;
  margin-left: -11px;
  border-bottom-width: 0;
  border-top-color: #999999;
  border-top-color: rgba(0, 0, 0, 0.25);
  bottom: -11px;
}
.popover.top > .arrow:after {
  content: " ";
  bottom: 1px;
  margin-left: -10px;
  border-bottom-width: 0;
  border-top-color: #fff;
}
.popover.right > .arrow {
  top: 50%;
  left: -11px;
  margin-top: -11px;
  border-left-width: 0;
  border-right-color: #999999;
  border-right-color: rgba(0, 0, 0, 0.25);
}
.popover.right > .arrow:after {
  content: " ";
  left: 1px;
  bottom: -10px;
  border-left-width: 0;
  border-right-color: #fff;
}
.popover.bottom > .arrow {
  left: 50%;
  margin-left: -11px;
  border-top-width: 0;
  border-bottom-color: #999999;
  border-bottom-color: rgba(0, 0, 0, 0.25);
  top: -11px;
}
.popover.bottom > .arrow:after {
  content: " ";
  top: 1px;
  margin-left: -10px;
  border-top-width: 0;
  border-bottom-color: #fff;
}
.popover.left > .arrow {
  top: 50%;
  right: -11px;
  margin-top: -11px;
  border-right-width: 0;
  border-left-color: #999999;
  border-left-color: rgba(0, 0, 0, 0.25);
}
.popover.left > .arrow:after {
  content: " ";
  right: 1px;
  border-right-width: 0;
  border-left-color: #fff;
  bottom: -10px;
}
.carousel {
  position: relative;
}
.carousel-inner {
  position: relative;
  overflow: hidden;
  width: 100%;
}
.carousel-inner > .item {
  display: none;
  position: relative;
  -webkit-transition: 0.6s ease-in-out left;
  -o-transition: 0.6s ease-in-out left;
  transition: 0.6s ease-in-out left;
}
.carousel-inner > .item > img,
.carousel-inner > .item > a > img {
  line-height: 1;
}
@media all and (transform-3d), (-webkit-transform-3d) {
  .carousel-inner > .item {
    -webkit-transition: -webkit-transform 0.6s ease-in-out;
    -moz-transition: -moz-transform 0.6s ease-in-out;
    -o-transition: -o-transform 0.6s ease-in-out;
    transition: transform 0.6s ease-in-out;
    -webkit-backface-visibility: hidden;
    -moz-backface-visibility: hidden;
    backface-visibility: hidden;
    -webkit-perspective: 1000px;
    -moz-perspective: 1000px;
    perspective: 1000px;
  }
  .carousel-inner > .item.next,
  .carousel-inner > .item.active.right {
    -webkit-transform: translate3d(100%, 0, 0);
    transform: translate3d(100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.prev,
  .carousel-inner > .item.active.left {
    -webkit-transform: translate3d(-100%, 0, 0);
    transform: translate3d(-100%, 0, 0);
    left: 0;
  }
  .carousel-inner > .item.next.left,
  .carousel-inner > .item.prev.right,
  .carousel-inner > .item.active {
    -webkit-transform: translate3d(0, 0, 0);
    transform: translate3d(0, 0, 0);
    left: 0;
  }
}
.carousel-inner > .active,
.carousel-inner > .next,
.carousel-inner > .prev {
  display: block;
}
.carousel-inner > .active {
  left: 0;
}
.carousel-inner > .next,
.carousel-inner > .prev {
  position: absolute;
  top: 0;
  width: 100%;
}
.carousel-inner > .next {
  left: 100%;
}
.carousel-inner > .prev {
  left: -100%;
}
.carousel-inner > .next.left,
.carousel-inner > .prev.right {
  left: 0;
}
.carousel-inner > .active.left {
  left: -100%;
}
.carousel-inner > .active.right {
  left: 100%;
}
.carousel-control {
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  width: 15%;
  opacity: 0.5;
  filter: alpha(opacity=50);
  font-size: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
  background-color: rgba(0, 0, 0, 0);
}
.carousel-control.left {
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.5) 0%, rgba(0, 0, 0, 0.0001) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#80000000', endColorstr='#00000000', GradientType=1);
}
.carousel-control.right {
  left: auto;
  right: 0;
  background-image: -webkit-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: -o-linear-gradient(left, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-image: linear-gradient(to right, rgba(0, 0, 0, 0.0001) 0%, rgba(0, 0, 0, 0.5) 100%);
  background-repeat: repeat-x;
  filter: progid:DXImageTransform.Microsoft.gradient(startColorstr='#00000000', endColorstr='#80000000', GradientType=1);
}
.carousel-control:hover,
.carousel-control:focus {
  outline: 0;
  color: #fff;
  text-decoration: none;
  opacity: 0.9;
  filter: alpha(opacity=90);
}
.carousel-control .icon-prev,
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-left,
.carousel-control .glyphicon-chevron-right {
  position: absolute;
  top: 50%;
  margin-top: -10px;
  z-index: 5;
  display: inline-block;
}
.carousel-control .icon-prev,
.carousel-control .glyphicon-chevron-left {
  left: 50%;
  margin-left: -10px;
}
.carousel-control .icon-next,
.carousel-control .glyphicon-chevron-right {
  right: 50%;
  margin-right: -10px;
}
.carousel-control .icon-prev,
.carousel-control .icon-next {
  width: 20px;
  height: 20px;
  line-height: 1;
  font-family: serif;
}
.carousel-control .icon-prev:before {
  content: '\2039';
}
.carousel-control .icon-next:before {
  content: '\203a';
}
.carousel-indicators {
  position: absolute;
  bottom: 10px;
  left: 50%;
  z-index: 15;
  width: 60%;
  margin-left: -30%;
  padding-left: 0;
  list-style: none;
  text-align: center;
}
.carousel-indicators li {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin: 1px;
  text-indent: -999px;
  border: 1px solid #fff;
  border-radius: 10px;
  cursor: pointer;
  background-color: #000 \9;
  background-color: rgba(0, 0, 0, 0);
}
.carousel-indicators .active {
  margin: 0;
  width: 12px;
  height: 12px;
  background-color: #fff;
}
.carousel-caption {
  position: absolute;
  left: 15%;
  right: 15%;
  bottom: 20px;
  z-index: 10;
  padding-top: 20px;
  padding-bottom: 20px;
  color: #fff;
  text-align: center;
  text-shadow: 0 1px 2px rgba(0, 0, 0, 0.6);
}
.carousel-caption .btn {
  text-shadow: none;
}
@media screen and (min-width: 768px) {
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-prev,
  .carousel-control .icon-next {
    width: 30px;
    height: 30px;
    margin-top: -10px;
    font-size: 30px;
  }
  .carousel-control .glyphicon-chevron-left,
  .carousel-control .icon-prev {
    margin-left: -10px;
  }
  .carousel-control .glyphicon-chevron-right,
  .carousel-control .icon-next {
    margin-right: -10px;
  }
  .carousel-caption {
    left: 20%;
    right: 20%;
    padding-bottom: 30px;
  }
  .carousel-indicators {
    bottom: 20px;
  }
}
.clearfix:before,
.clearfix:after,
.dl-horizontal dd:before,
.dl-horizontal dd:after,
.container:before,
.container:after,
.container-fluid:before,
.container-fluid:after,
.row:before,
.row:after,
.form-horizontal .form-group:before,
.form-horizontal .form-group:after,
.btn-toolbar:before,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:before,
.btn-group-vertical > .btn-group:after,
.nav:before,
.nav:after,
.navbar:before,
.navbar:after,
.navbar-header:before,
.navbar-header:after,
.navbar-collapse:before,
.navbar-collapse:after,
.pager:before,
.pager:after,
.panel-body:before,
.panel-body:after,
.modal-header:before,
.modal-header:after,
.modal-footer:before,
.modal-footer:after,
.item_buttons:before,
.item_buttons:after {
  content: " ";
  display: table;
}
.clearfix:after,
.dl-horizontal dd:after,
.container:after,
.container-fluid:after,
.row:after,
.form-horizontal .form-group:after,
.btn-toolbar:after,
.btn-group-vertical > .btn-group:after,
.nav:after,
.navbar:after,
.navbar-header:after,
.navbar-collapse:after,
.pager:after,
.panel-body:after,
.modal-header:after,
.modal-footer:after,
.item_buttons:after {
  clear: both;
}
.center-block {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.pull-right {
  float: right !important;
}
.pull-left {
  float: left !important;
}
.hide {
  display: none !important;
}
.show {
  display: block !important;
}
.invisible {
  visibility: hidden;
}
.text-hide {
  font: 0/0 a;
  color: transparent;
  text-shadow: none;
  background-color: transparent;
  border: 0;
}
.hidden {
  display: none !important;
}
.affix {
  position: fixed;
}
@-ms-viewport {
  width: device-width;
}
.visible-xs,
.visible-sm,
.visible-md,
.visible-lg {
  display: none !important;
}
.visible-xs-block,
.visible-xs-inline,
.visible-xs-inline-block,
.visible-sm-block,
.visible-sm-inline,
.visible-sm-inline-block,
.visible-md-block,
.visible-md-inline,
.visible-md-inline-block,
.visible-lg-block,
.visible-lg-inline,
.visible-lg-inline-block {
  display: none !important;
}
@media (max-width: 767px) {
  .visible-xs {
    display: block !important;
  }
  table.visible-xs {
    display: table !important;
  }
  tr.visible-xs {
    display: table-row !important;
  }
  th.visible-xs,
  td.visible-xs {
    display: table-cell !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-block {
    display: block !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline {
    display: inline !important;
  }
}
@media (max-width: 767px) {
  .visible-xs-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm {
    display: block !important;
  }
  table.visible-sm {
    display: table !important;
  }
  tr.visible-sm {
    display: table-row !important;
  }
  th.visible-sm,
  td.visible-sm {
    display: table-cell !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-block {
    display: block !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline {
    display: inline !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .visible-sm-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md {
    display: block !important;
  }
  table.visible-md {
    display: table !important;
  }
  tr.visible-md {
    display: table-row !important;
  }
  th.visible-md,
  td.visible-md {
    display: table-cell !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-block {
    display: block !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline {
    display: inline !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .visible-md-inline-block {
    display: inline-block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg {
    display: block !important;
  }
  table.visible-lg {
    display: table !important;
  }
  tr.visible-lg {
    display: table-row !important;
  }
  th.visible-lg,
  td.visible-lg {
    display: table-cell !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-block {
    display: block !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline {
    display: inline !important;
  }
}
@media (min-width: 1200px) {
  .visible-lg-inline-block {
    display: inline-block !important;
  }
}
@media (max-width: 767px) {
  .hidden-xs {
    display: none !important;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  .hidden-sm {
    display: none !important;
  }
}
@media (min-width: 992px) and (max-width: 1199px) {
  .hidden-md {
    display: none !important;
  }
}
@media (min-width: 1200px) {
  .hidden-lg {
    display: none !important;
  }
}
.visible-print {
  display: none !important;
}
@media print {
  .visible-print {
    display: block !important;
  }
  table.visible-print {
    display: table !important;
  }
  tr.visible-print {
    display: table-row !important;
  }
  th.visible-print,
  td.visible-print {
    display: table-cell !important;
  }
}
.visible-print-block {
  display: none !important;
}
@media print {
  .visible-print-block {
    display: block !important;
  }
}
.visible-print-inline {
  display: none !important;
}
@media print {
  .visible-print-inline {
    display: inline !important;
  }
}
.visible-print-inline-block {
  display: none !important;
}
@media print {
  .visible-print-inline-block {
    display: inline-block !important;
  }
}
@media print {
  .hidden-print {
    display: none !important;
  }
}
/*!
*
* Font Awesome
*
*/
/*!
 *  Font Awesome 4.7.0 by @davegandy - http://fontawesome.io - @fontawesome
 *  License - http://fontawesome.io/license (Font: SIL OFL 1.1, CSS: MIT License)
 */
/* FONT PATH
 * -------------------------- */
@font-face {
  font-family: 'FontAwesome';
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?v=4.7.0');
  src: url('../components/font-awesome/fonts/fontawesome-webfont.eot?#iefix&v=4.7.0') format('embedded-opentype'), url('../components/font-awesome/fonts/fontawesome-webfont.woff2?v=4.7.0') format('woff2'), url('../components/font-awesome/fonts/fontawesome-webfont.woff?v=4.7.0') format('woff'), url('../components/font-awesome/fonts/fontawesome-webfont.ttf?v=4.7.0') format('truetype'), url('../components/font-awesome/fonts/fontawesome-webfont.svg?v=4.7.0#fontawesomeregular') format('svg');
  font-weight: normal;
  font-style: normal;
}
.fa {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
/* makes the font 33% larger relative to the icon container */
.fa-lg {
  font-size: 1.33333333em;
  line-height: 0.75em;
  vertical-align: -15%;
}
.fa-2x {
  font-size: 2em;
}
.fa-3x {
  font-size: 3em;
}
.fa-4x {
  font-size: 4em;
}
.fa-5x {
  font-size: 5em;
}
.fa-fw {
  width: 1.28571429em;
  text-align: center;
}
.fa-ul {
  padding-left: 0;
  margin-left: 2.14285714em;
  list-style-type: none;
}
.fa-ul > li {
  position: relative;
}
.fa-li {
  position: absolute;
  left: -2.14285714em;
  width: 2.14285714em;
  top: 0.14285714em;
  text-align: center;
}
.fa-li.fa-lg {
  left: -1.85714286em;
}
.fa-border {
  padding: .2em .25em .15em;
  border: solid 0.08em #eee;
  border-radius: .1em;
}
.fa-pull-left {
  float: left;
}
.fa-pull-right {
  float: right;
}
.fa.fa-pull-left {
  margin-right: .3em;
}
.fa.fa-pull-right {
  margin-left: .3em;
}
/* Deprecated as of 4.4.0 */
.pull-right {
  float: right;
}
.pull-left {
  float: left;
}
.fa.pull-left {
  margin-right: .3em;
}
.fa.pull-right {
  margin-left: .3em;
}
.fa-spin {
  -webkit-animation: fa-spin 2s infinite linear;
  animation: fa-spin 2s infinite linear;
}
.fa-pulse {
  -webkit-animation: fa-spin 1s infinite steps(8);
  animation: fa-spin 1s infinite steps(8);
}
@-webkit-keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
@keyframes fa-spin {
  0% {
    -webkit-transform: rotate(0deg);
    transform: rotate(0deg);
  }
  100% {
    -webkit-transform: rotate(359deg);
    transform: rotate(359deg);
  }
}
.fa-rotate-90 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=1)";
  -webkit-transform: rotate(90deg);
  -ms-transform: rotate(90deg);
  transform: rotate(90deg);
}
.fa-rotate-180 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2)";
  -webkit-transform: rotate(180deg);
  -ms-transform: rotate(180deg);
  transform: rotate(180deg);
}
.fa-rotate-270 {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=3)";
  -webkit-transform: rotate(270deg);
  -ms-transform: rotate(270deg);
  transform: rotate(270deg);
}
.fa-flip-horizontal {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=0, mirror=1)";
  -webkit-transform: scale(-1, 1);
  -ms-transform: scale(-1, 1);
  transform: scale(-1, 1);
}
.fa-flip-vertical {
  -ms-filter: "progid:DXImageTransform.Microsoft.BasicImage(rotation=2, mirror=1)";
  -webkit-transform: scale(1, -1);
  -ms-transform: scale(1, -1);
  transform: scale(1, -1);
}
:root .fa-rotate-90,
:root .fa-rotate-180,
:root .fa-rotate-270,
:root .fa-flip-horizontal,
:root .fa-flip-vertical {
  filter: none;
}
.fa-stack {
  position: relative;
  display: inline-block;
  width: 2em;
  height: 2em;
  line-height: 2em;
  vertical-align: middle;
}
.fa-stack-1x,
.fa-stack-2x {
  position: absolute;
  left: 0;
  width: 100%;
  text-align: center;
}
.fa-stack-1x {
  line-height: inherit;
}
.fa-stack-2x {
  font-size: 2em;
}
.fa-inverse {
  color: #fff;
}
/* Font Awesome uses the Unicode Private Use Area (PUA) to ensure screen
   readers do not read off random characters that represent icons */
.fa-glass:before {
  content: "\f000";
}
.fa-music:before {
  content: "\f001";
}
.fa-search:before {
  content: "\f002";
}
.fa-envelope-o:before {
  content: "\f003";
}
.fa-heart:before {
  content: "\f004";
}
.fa-star:before {
  content: "\f005";
}
.fa-star-o:before {
  content: "\f006";
}
.fa-user:before {
  content: "\f007";
}
.fa-film:before {
  content: "\f008";
}
.fa-th-large:before {
  content: "\f009";
}
.fa-th:before {
  content: "\f00a";
}
.fa-th-list:before {
  content: "\f00b";
}
.fa-check:before {
  content: "\f00c";
}
.fa-remove:before,
.fa-close:before,
.fa-times:before {
  content: "\f00d";
}
.fa-search-plus:before {
  content: "\f00e";
}
.fa-search-minus:before {
  content: "\f010";
}
.fa-power-off:before {
  content: "\f011";
}
.fa-signal:before {
  content: "\f012";
}
.fa-gear:before,
.fa-cog:before {
  content: "\f013";
}
.fa-trash-o:before {
  content: "\f014";
}
.fa-home:before {
  content: "\f015";
}
.fa-file-o:before {
  content: "\f016";
}
.fa-clock-o:before {
  content: "\f017";
}
.fa-road:before {
  content: "\f018";
}
.fa-download:before {
  content: "\f019";
}
.fa-arrow-circle-o-down:before {
  content: "\f01a";
}
.fa-arrow-circle-o-up:before {
  content: "\f01b";
}
.fa-inbox:before {
  content: "\f01c";
}
.fa-play-circle-o:before {
  content: "\f01d";
}
.fa-rotate-right:before,
.fa-repeat:before {
  content: "\f01e";
}
.fa-refresh:before {
  content: "\f021";
}
.fa-list-alt:before {
  content: "\f022";
}
.fa-lock:before {
  content: "\f023";
}
.fa-flag:before {
  content: "\f024";
}
.fa-headphones:before {
  content: "\f025";
}
.fa-volume-off:before {
  content: "\f026";
}
.fa-volume-down:before {
  content: "\f027";
}
.fa-volume-up:before {
  content: "\f028";
}
.fa-qrcode:before {
  content: "\f029";
}
.fa-barcode:before {
  content: "\f02a";
}
.fa-tag:before {
  content: "\f02b";
}
.fa-tags:before {
  content: "\f02c";
}
.fa-book:before {
  content: "\f02d";
}
.fa-bookmark:before {
  content: "\f02e";
}
.fa-print:before {
  content: "\f02f";
}
.fa-camera:before {
  content: "\f030";
}
.fa-font:before {
  content: "\f031";
}
.fa-bold:before {
  content: "\f032";
}
.fa-italic:before {
  content: "\f033";
}
.fa-text-height:before {
  content: "\f034";
}
.fa-text-width:before {
  content: "\f035";
}
.fa-align-left:before {
  content: "\f036";
}
.fa-align-center:before {
  content: "\f037";
}
.fa-align-right:before {
  content: "\f038";
}
.fa-align-justify:before {
  content: "\f039";
}
.fa-list:before {
  content: "\f03a";
}
.fa-dedent:before,
.fa-outdent:before {
  content: "\f03b";
}
.fa-indent:before {
  content: "\f03c";
}
.fa-video-camera:before {
  content: "\f03d";
}
.fa-photo:before,
.fa-image:before,
.fa-picture-o:before {
  content: "\f03e";
}
.fa-pencil:before {
  content: "\f040";
}
.fa-map-marker:before {
  content: "\f041";
}
.fa-adjust:before {
  content: "\f042";
}
.fa-tint:before {
  content: "\f043";
}
.fa-edit:before,
.fa-pencil-square-o:before {
  content: "\f044";
}
.fa-share-square-o:before {
  content: "\f045";
}
.fa-check-square-o:before {
  content: "\f046";
}
.fa-arrows:before {
  content: "\f047";
}
.fa-step-backward:before {
  content: "\f048";
}
.fa-fast-backward:before {
  content: "\f049";
}
.fa-backward:before {
  content: "\f04a";
}
.fa-play:before {
  content: "\f04b";
}
.fa-pause:before {
  content: "\f04c";
}
.fa-stop:before {
  content: "\f04d";
}
.fa-forward:before {
  content: "\f04e";
}
.fa-fast-forward:before {
  content: "\f050";
}
.fa-step-forward:before {
  content: "\f051";
}
.fa-eject:before {
  content: "\f052";
}
.fa-chevron-left:before {
  content: "\f053";
}
.fa-chevron-right:before {
  content: "\f054";
}
.fa-plus-circle:before {
  content: "\f055";
}
.fa-minus-circle:before {
  content: "\f056";
}
.fa-times-circle:before {
  content: "\f057";
}
.fa-check-circle:before {
  content: "\f058";
}
.fa-question-circle:before {
  content: "\f059";
}
.fa-info-circle:before {
  content: "\f05a";
}
.fa-crosshairs:before {
  content: "\f05b";
}
.fa-times-circle-o:before {
  content: "\f05c";
}
.fa-check-circle-o:before {
  content: "\f05d";
}
.fa-ban:before {
  content: "\f05e";
}
.fa-arrow-left:before {
  content: "\f060";
}
.fa-arrow-right:before {
  content: "\f061";
}
.fa-arrow-up:before {
  content: "\f062";
}
.fa-arrow-down:before {
  content: "\f063";
}
.fa-mail-forward:before,
.fa-share:before {
  content: "\f064";
}
.fa-expand:before {
  content: "\f065";
}
.fa-compress:before {
  content: "\f066";
}
.fa-plus:before {
  content: "\f067";
}
.fa-minus:before {
  content: "\f068";
}
.fa-asterisk:before {
  content: "\f069";
}
.fa-exclamation-circle:before {
  content: "\f06a";
}
.fa-gift:before {
  content: "\f06b";
}
.fa-leaf:before {
  content: "\f06c";
}
.fa-fire:before {
  content: "\f06d";
}
.fa-eye:before {
  content: "\f06e";
}
.fa-eye-slash:before {
  content: "\f070";
}
.fa-warning:before,
.fa-exclamation-triangle:before {
  content: "\f071";
}
.fa-plane:before {
  content: "\f072";
}
.fa-calendar:before {
  content: "\f073";
}
.fa-random:before {
  content: "\f074";
}
.fa-comment:before {
  content: "\f075";
}
.fa-magnet:before {
  content: "\f076";
}
.fa-chevron-up:before {
  content: "\f077";
}
.fa-chevron-down:before {
  content: "\f078";
}
.fa-retweet:before {
  content: "\f079";
}
.fa-shopping-cart:before {
  content: "\f07a";
}
.fa-folder:before {
  content: "\f07b";
}
.fa-folder-open:before {
  content: "\f07c";
}
.fa-arrows-v:before {
  content: "\f07d";
}
.fa-arrows-h:before {
  content: "\f07e";
}
.fa-bar-chart-o:before,
.fa-bar-chart:before {
  content: "\f080";
}
.fa-twitter-square:before {
  content: "\f081";
}
.fa-facebook-square:before {
  content: "\f082";
}
.fa-camera-retro:before {
  content: "\f083";
}
.fa-key:before {
  content: "\f084";
}
.fa-gears:before,
.fa-cogs:before {
  content: "\f085";
}
.fa-comments:before {
  content: "\f086";
}
.fa-thumbs-o-up:before {
  content: "\f087";
}
.fa-thumbs-o-down:before {
  content: "\f088";
}
.fa-star-half:before {
  content: "\f089";
}
.fa-heart-o:before {
  content: "\f08a";
}
.fa-sign-out:before {
  content: "\f08b";
}
.fa-linkedin-square:before {
  content: "\f08c";
}
.fa-thumb-tack:before {
  content: "\f08d";
}
.fa-external-link:before {
  content: "\f08e";
}
.fa-sign-in:before {
  content: "\f090";
}
.fa-trophy:before {
  content: "\f091";
}
.fa-github-square:before {
  content: "\f092";
}
.fa-upload:before {
  content: "\f093";
}
.fa-lemon-o:before {
  content: "\f094";
}
.fa-phone:before {
  content: "\f095";
}
.fa-square-o:before {
  content: "\f096";
}
.fa-bookmark-o:before {
  content: "\f097";
}
.fa-phone-square:before {
  content: "\f098";
}
.fa-twitter:before {
  content: "\f099";
}
.fa-facebook-f:before,
.fa-facebook:before {
  content: "\f09a";
}
.fa-github:before {
  content: "\f09b";
}
.fa-unlock:before {
  content: "\f09c";
}
.fa-credit-card:before {
  content: "\f09d";
}
.fa-feed:before,
.fa-rss:before {
  content: "\f09e";
}
.fa-hdd-o:before {
  content: "\f0a0";
}
.fa-bullhorn:before {
  content: "\f0a1";
}
.fa-bell:before {
  content: "\f0f3";
}
.fa-certificate:before {
  content: "\f0a3";
}
.fa-hand-o-right:before {
  content: "\f0a4";
}
.fa-hand-o-left:before {
  content: "\f0a5";
}
.fa-hand-o-up:before {
  content: "\f0a6";
}
.fa-hand-o-down:before {
  content: "\f0a7";
}
.fa-arrow-circle-left:before {
  content: "\f0a8";
}
.fa-arrow-circle-right:before {
  content: "\f0a9";
}
.fa-arrow-circle-up:before {
  content: "\f0aa";
}
.fa-arrow-circle-down:before {
  content: "\f0ab";
}
.fa-globe:before {
  content: "\f0ac";
}
.fa-wrench:before {
  content: "\f0ad";
}
.fa-tasks:before {
  content: "\f0ae";
}
.fa-filter:before {
  content: "\f0b0";
}
.fa-briefcase:before {
  content: "\f0b1";
}
.fa-arrows-alt:before {
  content: "\f0b2";
}
.fa-group:before,
.fa-users:before {
  content: "\f0c0";
}
.fa-chain:before,
.fa-link:before {
  content: "\f0c1";
}
.fa-cloud:before {
  content: "\f0c2";
}
.fa-flask:before {
  content: "\f0c3";
}
.fa-cut:before,
.fa-scissors:before {
  content: "\f0c4";
}
.fa-copy:before,
.fa-files-o:before {
  content: "\f0c5";
}
.fa-paperclip:before {
  content: "\f0c6";
}
.fa-save:before,
.fa-floppy-o:before {
  content: "\f0c7";
}
.fa-square:before {
  content: "\f0c8";
}
.fa-navicon:before,
.fa-reorder:before,
.fa-bars:before {
  content: "\f0c9";
}
.fa-list-ul:before {
  content: "\f0ca";
}
.fa-list-ol:before {
  content: "\f0cb";
}
.fa-strikethrough:before {
  content: "\f0cc";
}
.fa-underline:before {
  content: "\f0cd";
}
.fa-table:before {
  content: "\f0ce";
}
.fa-magic:before {
  content: "\f0d0";
}
.fa-truck:before {
  content: "\f0d1";
}
.fa-pinterest:before {
  content: "\f0d2";
}
.fa-pinterest-square:before {
  content: "\f0d3";
}
.fa-google-plus-square:before {
  content: "\f0d4";
}
.fa-google-plus:before {
  content: "\f0d5";
}
.fa-money:before {
  content: "\f0d6";
}
.fa-caret-down:before {
  content: "\f0d7";
}
.fa-caret-up:before {
  content: "\f0d8";
}
.fa-caret-left:before {
  content: "\f0d9";
}
.fa-caret-right:before {
  content: "\f0da";
}
.fa-columns:before {
  content: "\f0db";
}
.fa-unsorted:before,
.fa-sort:before {
  content: "\f0dc";
}
.fa-sort-down:before,
.fa-sort-desc:before {
  content: "\f0dd";
}
.fa-sort-up:before,
.fa-sort-asc:before {
  content: "\f0de";
}
.fa-envelope:before {
  content: "\f0e0";
}
.fa-linkedin:before {
  content: "\f0e1";
}
.fa-rotate-left:before,
.fa-undo:before {
  content: "\f0e2";
}
.fa-legal:before,
.fa-gavel:before {
  content: "\f0e3";
}
.fa-dashboard:before,
.fa-tachometer:before {
  content: "\f0e4";
}
.fa-comment-o:before {
  content: "\f0e5";
}
.fa-comments-o:before {
  content: "\f0e6";
}
.fa-flash:before,
.fa-bolt:before {
  content: "\f0e7";
}
.fa-sitemap:before {
  content: "\f0e8";
}
.fa-umbrella:before {
  content: "\f0e9";
}
.fa-paste:before,
.fa-clipboard:before {
  content: "\f0ea";
}
.fa-lightbulb-o:before {
  content: "\f0eb";
}
.fa-exchange:before {
  content: "\f0ec";
}
.fa-cloud-download:before {
  content: "\f0ed";
}
.fa-cloud-upload:before {
  content: "\f0ee";
}
.fa-user-md:before {
  content: "\f0f0";
}
.fa-stethoscope:before {
  content: "\f0f1";
}
.fa-suitcase:before {
  content: "\f0f2";
}
.fa-bell-o:before {
  content: "\f0a2";
}
.fa-coffee:before {
  content: "\f0f4";
}
.fa-cutlery:before {
  content: "\f0f5";
}
.fa-file-text-o:before {
  content: "\f0f6";
}
.fa-building-o:before {
  content: "\f0f7";
}
.fa-hospital-o:before {
  content: "\f0f8";
}
.fa-ambulance:before {
  content: "\f0f9";
}
.fa-medkit:before {
  content: "\f0fa";
}
.fa-fighter-jet:before {
  content: "\f0fb";
}
.fa-beer:before {
  content: "\f0fc";
}
.fa-h-square:before {
  content: "\f0fd";
}
.fa-plus-square:before {
  content: "\f0fe";
}
.fa-angle-double-left:before {
  content: "\f100";
}
.fa-angle-double-right:before {
  content: "\f101";
}
.fa-angle-double-up:before {
  content: "\f102";
}
.fa-angle-double-down:before {
  content: "\f103";
}
.fa-angle-left:before {
  content: "\f104";
}
.fa-angle-right:before {
  content: "\f105";
}
.fa-angle-up:before {
  content: "\f106";
}
.fa-angle-down:before {
  content: "\f107";
}
.fa-desktop:before {
  content: "\f108";
}
.fa-laptop:before {
  content: "\f109";
}
.fa-tablet:before {
  content: "\f10a";
}
.fa-mobile-phone:before,
.fa-mobile:before {
  content: "\f10b";
}
.fa-circle-o:before {
  content: "\f10c";
}
.fa-quote-left:before {
  content: "\f10d";
}
.fa-quote-right:before {
  content: "\f10e";
}
.fa-spinner:before {
  content: "\f110";
}
.fa-circle:before {
  content: "\f111";
}
.fa-mail-reply:before,
.fa-reply:before {
  content: "\f112";
}
.fa-github-alt:before {
  content: "\f113";
}
.fa-folder-o:before {
  content: "\f114";
}
.fa-folder-open-o:before {
  content: "\f115";
}
.fa-smile-o:before {
  content: "\f118";
}
.fa-frown-o:before {
  content: "\f119";
}
.fa-meh-o:before {
  content: "\f11a";
}
.fa-gamepad:before {
  content: "\f11b";
}
.fa-keyboard-o:before {
  content: "\f11c";
}
.fa-flag-o:before {
  content: "\f11d";
}
.fa-flag-checkered:before {
  content: "\f11e";
}
.fa-terminal:before {
  content: "\f120";
}
.fa-code:before {
  content: "\f121";
}
.fa-mail-reply-all:before,
.fa-reply-all:before {
  content: "\f122";
}
.fa-star-half-empty:before,
.fa-star-half-full:before,
.fa-star-half-o:before {
  content: "\f123";
}
.fa-location-arrow:before {
  content: "\f124";
}
.fa-crop:before {
  content: "\f125";
}
.fa-code-fork:before {
  content: "\f126";
}
.fa-unlink:before,
.fa-chain-broken:before {
  content: "\f127";
}
.fa-question:before {
  content: "\f128";
}
.fa-info:before {
  content: "\f129";
}
.fa-exclamation:before {
  content: "\f12a";
}
.fa-superscript:before {
  content: "\f12b";
}
.fa-subscript:before {
  content: "\f12c";
}
.fa-eraser:before {
  content: "\f12d";
}
.fa-puzzle-piece:before {
  content: "\f12e";
}
.fa-microphone:before {
  content: "\f130";
}
.fa-microphone-slash:before {
  content: "\f131";
}
.fa-shield:before {
  content: "\f132";
}
.fa-calendar-o:before {
  content: "\f133";
}
.fa-fire-extinguisher:before {
  content: "\f134";
}
.fa-rocket:before {
  content: "\f135";
}
.fa-maxcdn:before {
  content: "\f136";
}
.fa-chevron-circle-left:before {
  content: "\f137";
}
.fa-chevron-circle-right:before {
  content: "\f138";
}
.fa-chevron-circle-up:before {
  content: "\f139";
}
.fa-chevron-circle-down:before {
  content: "\f13a";
}
.fa-html5:before {
  content: "\f13b";
}
.fa-css3:before {
  content: "\f13c";
}
.fa-anchor:before {
  content: "\f13d";
}
.fa-unlock-alt:before {
  content: "\f13e";
}
.fa-bullseye:before {
  content: "\f140";
}
.fa-ellipsis-h:before {
  content: "\f141";
}
.fa-ellipsis-v:before {
  content: "\f142";
}
.fa-rss-square:before {
  content: "\f143";
}
.fa-play-circle:before {
  content: "\f144";
}
.fa-ticket:before {
  content: "\f145";
}
.fa-minus-square:before {
  content: "\f146";
}
.fa-minus-square-o:before {
  content: "\f147";
}
.fa-level-up:before {
  content: "\f148";
}
.fa-level-down:before {
  content: "\f149";
}
.fa-check-square:before {
  content: "\f14a";
}
.fa-pencil-square:before {
  content: "\f14b";
}
.fa-external-link-square:before {
  content: "\f14c";
}
.fa-share-square:before {
  content: "\f14d";
}
.fa-compass:before {
  content: "\f14e";
}
.fa-toggle-down:before,
.fa-caret-square-o-down:before {
  content: "\f150";
}
.fa-toggle-up:before,
.fa-caret-square-o-up:before {
  content: "\f151";
}
.fa-toggle-right:before,
.fa-caret-square-o-right:before {
  content: "\f152";
}
.fa-euro:before,
.fa-eur:before {
  content: "\f153";
}
.fa-gbp:before {
  content: "\f154";
}
.fa-dollar:before,
.fa-usd:before {
  content: "\f155";
}
.fa-rupee:before,
.fa-inr:before {
  content: "\f156";
}
.fa-cny:before,
.fa-rmb:before,
.fa-yen:before,
.fa-jpy:before {
  content: "\f157";
}
.fa-ruble:before,
.fa-rouble:before,
.fa-rub:before {
  content: "\f158";
}
.fa-won:before,
.fa-krw:before {
  content: "\f159";
}
.fa-bitcoin:before,
.fa-btc:before {
  content: "\f15a";
}
.fa-file:before {
  content: "\f15b";
}
.fa-file-text:before {
  content: "\f15c";
}
.fa-sort-alpha-asc:before {
  content: "\f15d";
}
.fa-sort-alpha-desc:before {
  content: "\f15e";
}
.fa-sort-amount-asc:before {
  content: "\f160";
}
.fa-sort-amount-desc:before {
  content: "\f161";
}
.fa-sort-numeric-asc:before {
  content: "\f162";
}
.fa-sort-numeric-desc:before {
  content: "\f163";
}
.fa-thumbs-up:before {
  content: "\f164";
}
.fa-thumbs-down:before {
  content: "\f165";
}
.fa-youtube-square:before {
  content: "\f166";
}
.fa-youtube:before {
  content: "\f167";
}
.fa-xing:before {
  content: "\f168";
}
.fa-xing-square:before {
  content: "\f169";
}
.fa-youtube-play:before {
  content: "\f16a";
}
.fa-dropbox:before {
  content: "\f16b";
}
.fa-stack-overflow:before {
  content: "\f16c";
}
.fa-instagram:before {
  content: "\f16d";
}
.fa-flickr:before {
  content: "\f16e";
}
.fa-adn:before {
  content: "\f170";
}
.fa-bitbucket:before {
  content: "\f171";
}
.fa-bitbucket-square:before {
  content: "\f172";
}
.fa-tumblr:before {
  content: "\f173";
}
.fa-tumblr-square:before {
  content: "\f174";
}
.fa-long-arrow-down:before {
  content: "\f175";
}
.fa-long-arrow-up:before {
  content: "\f176";
}
.fa-long-arrow-left:before {
  content: "\f177";
}
.fa-long-arrow-right:before {
  content: "\f178";
}
.fa-apple:before {
  content: "\f179";
}
.fa-windows:before {
  content: "\f17a";
}
.fa-android:before {
  content: "\f17b";
}
.fa-linux:before {
  content: "\f17c";
}
.fa-dribbble:before {
  content: "\f17d";
}
.fa-skype:before {
  content: "\f17e";
}
.fa-foursquare:before {
  content: "\f180";
}
.fa-trello:before {
  content: "\f181";
}
.fa-female:before {
  content: "\f182";
}
.fa-male:before {
  content: "\f183";
}
.fa-gittip:before,
.fa-gratipay:before {
  content: "\f184";
}
.fa-sun-o:before {
  content: "\f185";
}
.fa-moon-o:before {
  content: "\f186";
}
.fa-archive:before {
  content: "\f187";
}
.fa-bug:before {
  content: "\f188";
}
.fa-vk:before {
  content: "\f189";
}
.fa-weibo:before {
  content: "\f18a";
}
.fa-renren:before {
  content: "\f18b";
}
.fa-pagelines:before {
  content: "\f18c";
}
.fa-stack-exchange:before {
  content: "\f18d";
}
.fa-arrow-circle-o-right:before {
  content: "\f18e";
}
.fa-arrow-circle-o-left:before {
  content: "\f190";
}
.fa-toggle-left:before,
.fa-caret-square-o-left:before {
  content: "\f191";
}
.fa-dot-circle-o:before {
  content: "\f192";
}
.fa-wheelchair:before {
  content: "\f193";
}
.fa-vimeo-square:before {
  content: "\f194";
}
.fa-turkish-lira:before,
.fa-try:before {
  content: "\f195";
}
.fa-plus-square-o:before {
  content: "\f196";
}
.fa-space-shuttle:before {
  content: "\f197";
}
.fa-slack:before {
  content: "\f198";
}
.fa-envelope-square:before {
  content: "\f199";
}
.fa-wordpress:before {
  content: "\f19a";
}
.fa-openid:before {
  content: "\f19b";
}
.fa-institution:before,
.fa-bank:before,
.fa-university:before {
  content: "\f19c";
}
.fa-mortar-board:before,
.fa-graduation-cap:before {
  content: "\f19d";
}
.fa-yahoo:before {
  content: "\f19e";
}
.fa-google:before {
  content: "\f1a0";
}
.fa-reddit:before {
  content: "\f1a1";
}
.fa-reddit-square:before {
  content: "\f1a2";
}
.fa-stumbleupon-circle:before {
  content: "\f1a3";
}
.fa-stumbleupon:before {
  content: "\f1a4";
}
.fa-delicious:before {
  content: "\f1a5";
}
.fa-digg:before {
  content: "\f1a6";
}
.fa-pied-piper-pp:before {
  content: "\f1a7";
}
.fa-pied-piper-alt:before {
  content: "\f1a8";
}
.fa-drupal:before {
  content: "\f1a9";
}
.fa-joomla:before {
  content: "\f1aa";
}
.fa-language:before {
  content: "\f1ab";
}
.fa-fax:before {
  content: "\f1ac";
}
.fa-building:before {
  content: "\f1ad";
}
.fa-child:before {
  content: "\f1ae";
}
.fa-paw:before {
  content: "\f1b0";
}
.fa-spoon:before {
  content: "\f1b1";
}
.fa-cube:before {
  content: "\f1b2";
}
.fa-cubes:before {
  content: "\f1b3";
}
.fa-behance:before {
  content: "\f1b4";
}
.fa-behance-square:before {
  content: "\f1b5";
}
.fa-steam:before {
  content: "\f1b6";
}
.fa-steam-square:before {
  content: "\f1b7";
}
.fa-recycle:before {
  content: "\f1b8";
}
.fa-automobile:before,
.fa-car:before {
  content: "\f1b9";
}
.fa-cab:before,
.fa-taxi:before {
  content: "\f1ba";
}
.fa-tree:before {
  content: "\f1bb";
}
.fa-spotify:before {
  content: "\f1bc";
}
.fa-deviantart:before {
  content: "\f1bd";
}
.fa-soundcloud:before {
  content: "\f1be";
}
.fa-database:before {
  content: "\f1c0";
}
.fa-file-pdf-o:before {
  content: "\f1c1";
}
.fa-file-word-o:before {
  content: "\f1c2";
}
.fa-file-excel-o:before {
  content: "\f1c3";
}
.fa-file-powerpoint-o:before {
  content: "\f1c4";
}
.fa-file-photo-o:before,
.fa-file-picture-o:before,
.fa-file-image-o:before {
  content: "\f1c5";
}
.fa-file-zip-o:before,
.fa-file-archive-o:before {
  content: "\f1c6";
}
.fa-file-sound-o:before,
.fa-file-audio-o:before {
  content: "\f1c7";
}
.fa-file-movie-o:before,
.fa-file-video-o:before {
  content: "\f1c8";
}
.fa-file-code-o:before {
  content: "\f1c9";
}
.fa-vine:before {
  content: "\f1ca";
}
.fa-codepen:before {
  content: "\f1cb";
}
.fa-jsfiddle:before {
  content: "\f1cc";
}
.fa-life-bouy:before,
.fa-life-buoy:before,
.fa-life-saver:before,
.fa-support:before,
.fa-life-ring:before {
  content: "\f1cd";
}
.fa-circle-o-notch:before {
  content: "\f1ce";
}
.fa-ra:before,
.fa-resistance:before,
.fa-rebel:before {
  content: "\f1d0";
}
.fa-ge:before,
.fa-empire:before {
  content: "\f1d1";
}
.fa-git-square:before {
  content: "\f1d2";
}
.fa-git:before {
  content: "\f1d3";
}
.fa-y-combinator-square:before,
.fa-yc-square:before,
.fa-hacker-news:before {
  content: "\f1d4";
}
.fa-tencent-weibo:before {
  content: "\f1d5";
}
.fa-qq:before {
  content: "\f1d6";
}
.fa-wechat:before,
.fa-weixin:before {
  content: "\f1d7";
}
.fa-send:before,
.fa-paper-plane:before {
  content: "\f1d8";
}
.fa-send-o:before,
.fa-paper-plane-o:before {
  content: "\f1d9";
}
.fa-history:before {
  content: "\f1da";
}
.fa-circle-thin:before {
  content: "\f1db";
}
.fa-header:before {
  content: "\f1dc";
}
.fa-paragraph:before {
  content: "\f1dd";
}
.fa-sliders:before {
  content: "\f1de";
}
.fa-share-alt:before {
  content: "\f1e0";
}
.fa-share-alt-square:before {
  content: "\f1e1";
}
.fa-bomb:before {
  content: "\f1e2";
}
.fa-soccer-ball-o:before,
.fa-futbol-o:before {
  content: "\f1e3";
}
.fa-tty:before {
  content: "\f1e4";
}
.fa-binoculars:before {
  content: "\f1e5";
}
.fa-plug:before {
  content: "\f1e6";
}
.fa-slideshare:before {
  content: "\f1e7";
}
.fa-twitch:before {
  content: "\f1e8";
}
.fa-yelp:before {
  content: "\f1e9";
}
.fa-newspaper-o:before {
  content: "\f1ea";
}
.fa-wifi:before {
  content: "\f1eb";
}
.fa-calculator:before {
  content: "\f1ec";
}
.fa-paypal:before {
  content: "\f1ed";
}
.fa-google-wallet:before {
  content: "\f1ee";
}
.fa-cc-visa:before {
  content: "\f1f0";
}
.fa-cc-mastercard:before {
  content: "\f1f1";
}
.fa-cc-discover:before {
  content: "\f1f2";
}
.fa-cc-amex:before {
  content: "\f1f3";
}
.fa-cc-paypal:before {
  content: "\f1f4";
}
.fa-cc-stripe:before {
  content: "\f1f5";
}
.fa-bell-slash:before {
  content: "\f1f6";
}
.fa-bell-slash-o:before {
  content: "\f1f7";
}
.fa-trash:before {
  content: "\f1f8";
}
.fa-copyright:before {
  content: "\f1f9";
}
.fa-at:before {
  content: "\f1fa";
}
.fa-eyedropper:before {
  content: "\f1fb";
}
.fa-paint-brush:before {
  content: "\f1fc";
}
.fa-birthday-cake:before {
  content: "\f1fd";
}
.fa-area-chart:before {
  content: "\f1fe";
}
.fa-pie-chart:before {
  content: "\f200";
}
.fa-line-chart:before {
  content: "\f201";
}
.fa-lastfm:before {
  content: "\f202";
}
.fa-lastfm-square:before {
  content: "\f203";
}
.fa-toggle-off:before {
  content: "\f204";
}
.fa-toggle-on:before {
  content: "\f205";
}
.fa-bicycle:before {
  content: "\f206";
}
.fa-bus:before {
  content: "\f207";
}
.fa-ioxhost:before {
  content: "\f208";
}
.fa-angellist:before {
  content: "\f209";
}
.fa-cc:before {
  content: "\f20a";
}
.fa-shekel:before,
.fa-sheqel:before,
.fa-ils:before {
  content: "\f20b";
}
.fa-meanpath:before {
  content: "\f20c";
}
.fa-buysellads:before {
  content: "\f20d";
}
.fa-connectdevelop:before {
  content: "\f20e";
}
.fa-dashcube:before {
  content: "\f210";
}
.fa-forumbee:before {
  content: "\f211";
}
.fa-leanpub:before {
  content: "\f212";
}
.fa-sellsy:before {
  content: "\f213";
}
.fa-shirtsinbulk:before {
  content: "\f214";
}
.fa-simplybuilt:before {
  content: "\f215";
}
.fa-skyatlas:before {
  content: "\f216";
}
.fa-cart-plus:before {
  content: "\f217";
}
.fa-cart-arrow-down:before {
  content: "\f218";
}
.fa-diamond:before {
  content: "\f219";
}
.fa-ship:before {
  content: "\f21a";
}
.fa-user-secret:before {
  content: "\f21b";
}
.fa-motorcycle:before {
  content: "\f21c";
}
.fa-street-view:before {
  content: "\f21d";
}
.fa-heartbeat:before {
  content: "\f21e";
}
.fa-venus:before {
  content: "\f221";
}
.fa-mars:before {
  content: "\f222";
}
.fa-mercury:before {
  content: "\f223";
}
.fa-intersex:before,
.fa-transgender:before {
  content: "\f224";
}
.fa-transgender-alt:before {
  content: "\f225";
}
.fa-venus-double:before {
  content: "\f226";
}
.fa-mars-double:before {
  content: "\f227";
}
.fa-venus-mars:before {
  content: "\f228";
}
.fa-mars-stroke:before {
  content: "\f229";
}
.fa-mars-stroke-v:before {
  content: "\f22a";
}
.fa-mars-stroke-h:before {
  content: "\f22b";
}
.fa-neuter:before {
  content: "\f22c";
}
.fa-genderless:before {
  content: "\f22d";
}
.fa-facebook-official:before {
  content: "\f230";
}
.fa-pinterest-p:before {
  content: "\f231";
}
.fa-whatsapp:before {
  content: "\f232";
}
.fa-server:before {
  content: "\f233";
}
.fa-user-plus:before {
  content: "\f234";
}
.fa-user-times:before {
  content: "\f235";
}
.fa-hotel:before,
.fa-bed:before {
  content: "\f236";
}
.fa-viacoin:before {
  content: "\f237";
}
.fa-train:before {
  content: "\f238";
}
.fa-subway:before {
  content: "\f239";
}
.fa-medium:before {
  content: "\f23a";
}
.fa-yc:before,
.fa-y-combinator:before {
  content: "\f23b";
}
.fa-optin-monster:before {
  content: "\f23c";
}
.fa-opencart:before {
  content: "\f23d";
}
.fa-expeditedssl:before {
  content: "\f23e";
}
.fa-battery-4:before,
.fa-battery:before,
.fa-battery-full:before {
  content: "\f240";
}
.fa-battery-3:before,
.fa-battery-three-quarters:before {
  content: "\f241";
}
.fa-battery-2:before,
.fa-battery-half:before {
  content: "\f242";
}
.fa-battery-1:before,
.fa-battery-quarter:before {
  content: "\f243";
}
.fa-battery-0:before,
.fa-battery-empty:before {
  content: "\f244";
}
.fa-mouse-pointer:before {
  content: "\f245";
}
.fa-i-cursor:before {
  content: "\f246";
}
.fa-object-group:before {
  content: "\f247";
}
.fa-object-ungroup:before {
  content: "\f248";
}
.fa-sticky-note:before {
  content: "\f249";
}
.fa-sticky-note-o:before {
  content: "\f24a";
}
.fa-cc-jcb:before {
  content: "\f24b";
}
.fa-cc-diners-club:before {
  content: "\f24c";
}
.fa-clone:before {
  content: "\f24d";
}
.fa-balance-scale:before {
  content: "\f24e";
}
.fa-hourglass-o:before {
  content: "\f250";
}
.fa-hourglass-1:before,
.fa-hourglass-start:before {
  content: "\f251";
}
.fa-hourglass-2:before,
.fa-hourglass-half:before {
  content: "\f252";
}
.fa-hourglass-3:before,
.fa-hourglass-end:before {
  content: "\f253";
}
.fa-hourglass:before {
  content: "\f254";
}
.fa-hand-grab-o:before,
.fa-hand-rock-o:before {
  content: "\f255";
}
.fa-hand-stop-o:before,
.fa-hand-paper-o:before {
  content: "\f256";
}
.fa-hand-scissors-o:before {
  content: "\f257";
}
.fa-hand-lizard-o:before {
  content: "\f258";
}
.fa-hand-spock-o:before {
  content: "\f259";
}
.fa-hand-pointer-o:before {
  content: "\f25a";
}
.fa-hand-peace-o:before {
  content: "\f25b";
}
.fa-trademark:before {
  content: "\f25c";
}
.fa-registered:before {
  content: "\f25d";
}
.fa-creative-commons:before {
  content: "\f25e";
}
.fa-gg:before {
  content: "\f260";
}
.fa-gg-circle:before {
  content: "\f261";
}
.fa-tripadvisor:before {
  content: "\f262";
}
.fa-odnoklassniki:before {
  content: "\f263";
}
.fa-odnoklassniki-square:before {
  content: "\f264";
}
.fa-get-pocket:before {
  content: "\f265";
}
.fa-wikipedia-w:before {
  content: "\f266";
}
.fa-safari:before {
  content: "\f267";
}
.fa-chrome:before {
  content: "\f268";
}
.fa-firefox:before {
  content: "\f269";
}
.fa-opera:before {
  content: "\f26a";
}
.fa-internet-explorer:before {
  content: "\f26b";
}
.fa-tv:before,
.fa-television:before {
  content: "\f26c";
}
.fa-contao:before {
  content: "\f26d";
}
.fa-500px:before {
  content: "\f26e";
}
.fa-amazon:before {
  content: "\f270";
}
.fa-calendar-plus-o:before {
  content: "\f271";
}
.fa-calendar-minus-o:before {
  content: "\f272";
}
.fa-calendar-times-o:before {
  content: "\f273";
}
.fa-calendar-check-o:before {
  content: "\f274";
}
.fa-industry:before {
  content: "\f275";
}
.fa-map-pin:before {
  content: "\f276";
}
.fa-map-signs:before {
  content: "\f277";
}
.fa-map-o:before {
  content: "\f278";
}
.fa-map:before {
  content: "\f279";
}
.fa-commenting:before {
  content: "\f27a";
}
.fa-commenting-o:before {
  content: "\f27b";
}
.fa-houzz:before {
  content: "\f27c";
}
.fa-vimeo:before {
  content: "\f27d";
}
.fa-black-tie:before {
  content: "\f27e";
}
.fa-fonticons:before {
  content: "\f280";
}
.fa-reddit-alien:before {
  content: "\f281";
}
.fa-edge:before {
  content: "\f282";
}
.fa-credit-card-alt:before {
  content: "\f283";
}
.fa-codiepie:before {
  content: "\f284";
}
.fa-modx:before {
  content: "\f285";
}
.fa-fort-awesome:before {
  content: "\f286";
}
.fa-usb:before {
  content: "\f287";
}
.fa-product-hunt:before {
  content: "\f288";
}
.fa-mixcloud:before {
  content: "\f289";
}
.fa-scribd:before {
  content: "\f28a";
}
.fa-pause-circle:before {
  content: "\f28b";
}
.fa-pause-circle-o:before {
  content: "\f28c";
}
.fa-stop-circle:before {
  content: "\f28d";
}
.fa-stop-circle-o:before {
  content: "\f28e";
}
.fa-shopping-bag:before {
  content: "\f290";
}
.fa-shopping-basket:before {
  content: "\f291";
}
.fa-hashtag:before {
  content: "\f292";
}
.fa-bluetooth:before {
  content: "\f293";
}
.fa-bluetooth-b:before {
  content: "\f294";
}
.fa-percent:before {
  content: "\f295";
}
.fa-gitlab:before {
  content: "\f296";
}
.fa-wpbeginner:before {
  content: "\f297";
}
.fa-wpforms:before {
  content: "\f298";
}
.fa-envira:before {
  content: "\f299";
}
.fa-universal-access:before {
  content: "\f29a";
}
.fa-wheelchair-alt:before {
  content: "\f29b";
}
.fa-question-circle-o:before {
  content: "\f29c";
}
.fa-blind:before {
  content: "\f29d";
}
.fa-audio-description:before {
  content: "\f29e";
}
.fa-volume-control-phone:before {
  content: "\f2a0";
}
.fa-braille:before {
  content: "\f2a1";
}
.fa-assistive-listening-systems:before {
  content: "\f2a2";
}
.fa-asl-interpreting:before,
.fa-american-sign-language-interpreting:before {
  content: "\f2a3";
}
.fa-deafness:before,
.fa-hard-of-hearing:before,
.fa-deaf:before {
  content: "\f2a4";
}
.fa-glide:before {
  content: "\f2a5";
}
.fa-glide-g:before {
  content: "\f2a6";
}
.fa-signing:before,
.fa-sign-language:before {
  content: "\f2a7";
}
.fa-low-vision:before {
  content: "\f2a8";
}
.fa-viadeo:before {
  content: "\f2a9";
}
.fa-viadeo-square:before {
  content: "\f2aa";
}
.fa-snapchat:before {
  content: "\f2ab";
}
.fa-snapchat-ghost:before {
  content: "\f2ac";
}
.fa-snapchat-square:before {
  content: "\f2ad";
}
.fa-pied-piper:before {
  content: "\f2ae";
}
.fa-first-order:before {
  content: "\f2b0";
}
.fa-yoast:before {
  content: "\f2b1";
}
.fa-themeisle:before {
  content: "\f2b2";
}
.fa-google-plus-circle:before,
.fa-google-plus-official:before {
  content: "\f2b3";
}
.fa-fa:before,
.fa-font-awesome:before {
  content: "\f2b4";
}
.fa-handshake-o:before {
  content: "\f2b5";
}
.fa-envelope-open:before {
  content: "\f2b6";
}
.fa-envelope-open-o:before {
  content: "\f2b7";
}
.fa-linode:before {
  content: "\f2b8";
}
.fa-address-book:before {
  content: "\f2b9";
}
.fa-address-book-o:before {
  content: "\f2ba";
}
.fa-vcard:before,
.fa-address-card:before {
  content: "\f2bb";
}
.fa-vcard-o:before,
.fa-address-card-o:before {
  content: "\f2bc";
}
.fa-user-circle:before {
  content: "\f2bd";
}
.fa-user-circle-o:before {
  content: "\f2be";
}
.fa-user-o:before {
  content: "\f2c0";
}
.fa-id-badge:before {
  content: "\f2c1";
}
.fa-drivers-license:before,
.fa-id-card:before {
  content: "\f2c2";
}
.fa-drivers-license-o:before,
.fa-id-card-o:before {
  content: "\f2c3";
}
.fa-quora:before {
  content: "\f2c4";
}
.fa-free-code-camp:before {
  content: "\f2c5";
}
.fa-telegram:before {
  content: "\f2c6";
}
.fa-thermometer-4:before,
.fa-thermometer:before,
.fa-thermometer-full:before {
  content: "\f2c7";
}
.fa-thermometer-3:before,
.fa-thermometer-three-quarters:before {
  content: "\f2c8";
}
.fa-thermometer-2:before,
.fa-thermometer-half:before {
  content: "\f2c9";
}
.fa-thermometer-1:before,
.fa-thermometer-quarter:before {
  content: "\f2ca";
}
.fa-thermometer-0:before,
.fa-thermometer-empty:before {
  content: "\f2cb";
}
.fa-shower:before {
  content: "\f2cc";
}
.fa-bathtub:before,
.fa-s15:before,
.fa-bath:before {
  content: "\f2cd";
}
.fa-podcast:before {
  content: "\f2ce";
}
.fa-window-maximize:before {
  content: "\f2d0";
}
.fa-window-minimize:before {
  content: "\f2d1";
}
.fa-window-restore:before {
  content: "\f2d2";
}
.fa-times-rectangle:before,
.fa-window-close:before {
  content: "\f2d3";
}
.fa-times-rectangle-o:before,
.fa-window-close-o:before {
  content: "\f2d4";
}
.fa-bandcamp:before {
  content: "\f2d5";
}
.fa-grav:before {
  content: "\f2d6";
}
.fa-etsy:before {
  content: "\f2d7";
}
.fa-imdb:before {
  content: "\f2d8";
}
.fa-ravelry:before {
  content: "\f2d9";
}
.fa-eercast:before {
  content: "\f2da";
}
.fa-microchip:before {
  content: "\f2db";
}
.fa-snowflake-o:before {
  content: "\f2dc";
}
.fa-superpowers:before {
  content: "\f2dd";
}
.fa-wpexplorer:before {
  content: "\f2de";
}
.fa-meetup:before {
  content: "\f2e0";
}
.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
.sr-only-focusable:active,
.sr-only-focusable:focus {
  position: static;
  width: auto;
  height: auto;
  margin: 0;
  overflow: visible;
  clip: auto;
}
/*!
*
* IPython base
*
*/
.modal.fade .modal-dialog {
  -webkit-transform: translate(0, 0);
  -ms-transform: translate(0, 0);
  -o-transform: translate(0, 0);
  transform: translate(0, 0);
}
code {
  color: #000;
}
pre {
  font-size: inherit;
  line-height: inherit;
}
label {
  font-weight: normal;
}
/* Make the page background atleast 100% the height of the view port */
/* Make the page itself atleast 70% the height of the view port */
.border-box-sizing {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.corner-all {
  border-radius: 2px;
}
.no-padding {
  padding: 0px;
}
/* Flexible box model classes */
/* Taken from Alex Russell http://infrequently.org/2009/08/css-3-progress/ */
/* This file is a compatability layer.  It allows the usage of flexible box 
model layouts accross multiple browsers, including older browsers.  The newest,
universal implementation of the flexible box model is used when available (see
`Modern browsers` comments below).  Browsers that are known to implement this 
new spec completely include:

    Firefox 28.0+
    Chrome 29.0+
    Internet Explorer 11+ 
    Opera 17.0+

Browsers not listed, including Safari, are supported via the styling under the
`Old browsers` comments below.
*/
.hbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
.hbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.vbox {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
.vbox > * {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
}
.hbox.reverse,
.vbox.reverse,
.reverse {
  /* Old browsers */
  -webkit-box-direction: reverse;
  -moz-box-direction: reverse;
  box-direction: reverse;
  /* Modern browsers */
  flex-direction: row-reverse;
}
.hbox.box-flex0,
.vbox.box-flex0,
.box-flex0 {
  /* Old browsers */
  -webkit-box-flex: 0;
  -moz-box-flex: 0;
  box-flex: 0;
  /* Modern browsers */
  flex: none;
  width: auto;
}
.hbox.box-flex1,
.vbox.box-flex1,
.box-flex1 {
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex,
.vbox.box-flex,
.box-flex {
  /* Old browsers */
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
.hbox.box-flex2,
.vbox.box-flex2,
.box-flex2 {
  /* Old browsers */
  -webkit-box-flex: 2;
  -moz-box-flex: 2;
  box-flex: 2;
  /* Modern browsers */
  flex: 2;
}
.box-group1 {
  /*  Deprecated */
  -webkit-box-flex-group: 1;
  -moz-box-flex-group: 1;
  box-flex-group: 1;
}
.box-group2 {
  /* Deprecated */
  -webkit-box-flex-group: 2;
  -moz-box-flex-group: 2;
  box-flex-group: 2;
}
.hbox.start,
.vbox.start,
.start {
  /* Old browsers */
  -webkit-box-pack: start;
  -moz-box-pack: start;
  box-pack: start;
  /* Modern browsers */
  justify-content: flex-start;
}
.hbox.end,
.vbox.end,
.end {
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
}
.hbox.center,
.vbox.center,
.center {
  /* Old browsers */
  -webkit-box-pack: center;
  -moz-box-pack: center;
  box-pack: center;
  /* Modern browsers */
  justify-content: center;
}
.hbox.baseline,
.vbox.baseline,
.baseline {
  /* Old browsers */
  -webkit-box-pack: baseline;
  -moz-box-pack: baseline;
  box-pack: baseline;
  /* Modern browsers */
  justify-content: baseline;
}
.hbox.stretch,
.vbox.stretch,
.stretch {
  /* Old browsers */
  -webkit-box-pack: stretch;
  -moz-box-pack: stretch;
  box-pack: stretch;
  /* Modern browsers */
  justify-content: stretch;
}
.hbox.align-start,
.vbox.align-start,
.align-start {
  /* Old browsers */
  -webkit-box-align: start;
  -moz-box-align: start;
  box-align: start;
  /* Modern browsers */
  align-items: flex-start;
}
.hbox.align-end,
.vbox.align-end,
.align-end {
  /* Old browsers */
  -webkit-box-align: end;
  -moz-box-align: end;
  box-align: end;
  /* Modern browsers */
  align-items: flex-end;
}
.hbox.align-center,
.vbox.align-center,
.align-center {
  /* Old browsers */
  -webkit-box-align: center;
  -moz-box-align: center;
  box-align: center;
  /* Modern browsers */
  align-items: center;
}
.hbox.align-baseline,
.vbox.align-baseline,
.align-baseline {
  /* Old browsers */
  -webkit-box-align: baseline;
  -moz-box-align: baseline;
  box-align: baseline;
  /* Modern browsers */
  align-items: baseline;
}
.hbox.align-stretch,
.vbox.align-stretch,
.align-stretch {
  /* Old browsers */
  -webkit-box-align: stretch;
  -moz-box-align: stretch;
  box-align: stretch;
  /* Modern browsers */
  align-items: stretch;
}
div.error {
  margin: 2em;
  text-align: center;
}
div.error > h1 {
  font-size: 500%;
  line-height: normal;
}
div.error > p {
  font-size: 200%;
  line-height: normal;
}
div.traceback-wrapper {
  text-align: left;
  max-width: 800px;
  margin: auto;
}
div.traceback-wrapper pre.traceback {
  max-height: 600px;
  overflow: auto;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
body {
  background-color: #fff;
  /* This makes sure that the body covers the entire window and needs to
       be in a different element than the display: box in wrapper below */
  position: absolute;
  left: 0px;
  right: 0px;
  top: 0px;
  bottom: 0px;
  overflow: visible;
}
body > #header {
  /* Initially hidden to prevent FLOUC */
  display: none;
  background-color: #fff;
  /* Display over codemirror */
  position: relative;
  z-index: 100;
}
body > #header #header-container {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  padding: 5px;
  padding-bottom: 5px;
  padding-top: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
body > #header .header-bar {
  width: 100%;
  height: 1px;
  background: #e7e7e7;
  margin-bottom: -1px;
}
@media print {
  body > #header {
    display: none !important;
  }
}
#header-spacer {
  width: 100%;
  visibility: hidden;
}
@media print {
  #header-spacer {
    display: none;
  }
}
#ipython_notebook {
  padding-left: 0px;
  padding-top: 1px;
  padding-bottom: 1px;
}
[dir="rtl"] #ipython_notebook {
  margin-right: 10px;
  margin-left: 0;
}
[dir="rtl"] #ipython_notebook.pull-left {
  float: right !important;
  float: right;
}
.flex-spacer {
  flex: 1;
}
#noscript {
  width: auto;
  padding-top: 16px;
  padding-bottom: 16px;
  text-align: center;
  font-size: 22px;
  color: red;
  font-weight: bold;
}
#ipython_notebook img {
  height: 28px;
}
#site {
  width: 100%;
  display: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  overflow: auto;
}
@media print {
  #site {
    height: auto !important;
  }
}
/* Smaller buttons */
.ui-button .ui-button-text {
  padding: 0.2em 0.8em;
  font-size: 77%;
}
input.ui-button {
  padding: 0.3em 0.9em;
}
span#kernel_logo_widget {
  margin: 0 10px;
}
span#login_widget {
  float: right;
}
[dir="rtl"] span#login_widget {
  float: left;
}
span#login_widget > .button,
#logout {
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button:focus,
#logout:focus,
span#login_widget > .button.focus,
#logout.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
span#login_widget > .button:hover,
#logout:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
span#login_widget > .button:active:hover,
#logout:active:hover,
span#login_widget > .button.active:hover,
#logout.active:hover,
.open > .dropdown-togglespan#login_widget > .button:hover,
.open > .dropdown-toggle#logout:hover,
span#login_widget > .button:active:focus,
#logout:active:focus,
span#login_widget > .button.active:focus,
#logout.active:focus,
.open > .dropdown-togglespan#login_widget > .button:focus,
.open > .dropdown-toggle#logout:focus,
span#login_widget > .button:active.focus,
#logout:active.focus,
span#login_widget > .button.active.focus,
#logout.active.focus,
.open > .dropdown-togglespan#login_widget > .button.focus,
.open > .dropdown-toggle#logout.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
span#login_widget > .button:active,
#logout:active,
span#login_widget > .button.active,
#logout.active,
.open > .dropdown-togglespan#login_widget > .button,
.open > .dropdown-toggle#logout {
  background-image: none;
}
span#login_widget > .button.disabled:hover,
#logout.disabled:hover,
span#login_widget > .button[disabled]:hover,
#logout[disabled]:hover,
fieldset[disabled] span#login_widget > .button:hover,
fieldset[disabled] #logout:hover,
span#login_widget > .button.disabled:focus,
#logout.disabled:focus,
span#login_widget > .button[disabled]:focus,
#logout[disabled]:focus,
fieldset[disabled] span#login_widget > .button:focus,
fieldset[disabled] #logout:focus,
span#login_widget > .button.disabled.focus,
#logout.disabled.focus,
span#login_widget > .button[disabled].focus,
#logout[disabled].focus,
fieldset[disabled] span#login_widget > .button.focus,
fieldset[disabled] #logout.focus {
  background-color: #fff;
  border-color: #ccc;
}
span#login_widget > .button .badge,
#logout .badge {
  color: #fff;
  background-color: #333;
}
.nav-header {
  text-transform: none;
}
#header > span {
  margin-top: 10px;
}
.modal_stretch .modal-dialog {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  min-height: 80vh;
}
.modal_stretch .modal-dialog .modal-body {
  max-height: calc(100vh - 200px);
  overflow: auto;
  flex: 1;
}
.modal-header {
  cursor: move;
}
@media (min-width: 768px) {
  .modal .modal-dialog {
    width: 700px;
  }
}
@media (min-width: 768px) {
  select.form-control {
    margin-left: 12px;
    margin-right: 12px;
  }
}
/*!
*
* IPython auth
*
*/
.center-nav {
  display: inline-block;
  margin-bottom: -4px;
}
[dir="rtl"] .center-nav form.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] .center-nav .navbar-text {
  float: right;
}
[dir="rtl"] .navbar-inner {
  text-align: right;
}
[dir="rtl"] div.text-left {
  text-align: right;
}
/*!
*
* IPython tree view
*
*/
/* We need an invisible input field on top of the sentense*/
/* "Drag file onto the list ..." */
.alternate_upload {
  background-color: none;
  display: inline;
}
.alternate_upload.form {
  padding: 0;
  margin: 0;
}
.alternate_upload input.fileinput {
  position: absolute;
  display: block;
  width: 100%;
  height: 100%;
  overflow: hidden;
  cursor: pointer;
  opacity: 0;
  z-index: 2;
}
.alternate_upload .btn-xs > input.fileinput {
  margin: -1px -5px;
}
.alternate_upload .btn-upload {
  position: relative;
  height: 22px;
}
::-webkit-file-upload-button {
  cursor: pointer;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
ul#tabs {
  margin-bottom: 4px;
}
ul#tabs a {
  padding-top: 6px;
  padding-bottom: 4px;
}
[dir="rtl"] ul#tabs.nav-tabs > li {
  float: right;
}
[dir="rtl"] ul#tabs.nav.nav-tabs {
  padding-right: 0;
}
ul.breadcrumb a:focus,
ul.breadcrumb a:hover {
  text-decoration: none;
}
ul.breadcrumb i.icon-home {
  font-size: 16px;
  margin-right: 4px;
}
ul.breadcrumb span {
  color: #5e5e5e;
}
.list_toolbar {
  padding: 4px 0 4px 0;
  vertical-align: middle;
}
.list_toolbar .tree-buttons {
  padding-top: 1px;
}
[dir="rtl"] .list_toolbar .tree-buttons .pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .list_toolbar .col-sm-4,
[dir="rtl"] .list_toolbar .col-sm-8 {
  float: right;
}
.dynamic-buttons {
  padding-top: 3px;
  display: inline-block;
}
.list_toolbar [class*="span"] {
  min-height: 24px;
}
.list_header {
  font-weight: bold;
  background-color: #EEE;
}
.list_placeholder {
  font-weight: bold;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
}
.list_container {
  margin-top: 4px;
  margin-bottom: 20px;
  border: 1px solid #ddd;
  border-radius: 2px;
}
.list_container > div {
  border-bottom: 1px solid #ddd;
}
.list_container > div:hover .list-item {
  background-color: red;
}
.list_container > div:last-child {
  border: none;
}
.list_item:hover .list_item {
  background-color: #ddd;
}
.list_item a {
  text-decoration: none;
}
.list_item:hover {
  background-color: #fafafa;
}
.list_header > div,
.list_item > div {
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
.list_header > div input,
.list_item > div input {
  margin-right: 7px;
  margin-left: 14px;
  vertical-align: text-bottom;
  line-height: 22px;
  position: relative;
  top: -1px;
}
.list_header > div .item_link,
.list_item > div .item_link {
  margin-left: -1px;
  vertical-align: baseline;
  line-height: 22px;
}
[dir="rtl"] .list_item > div input {
  margin-right: 0;
}
.new-file input[type=checkbox] {
  visibility: hidden;
}
.item_name {
  line-height: 22px;
  height: 24px;
}
.item_icon {
  font-size: 14px;
  color: #5e5e5e;
  margin-right: 7px;
  margin-left: 7px;
  line-height: 22px;
  vertical-align: baseline;
}
.item_modified {
  margin-right: 7px;
  margin-left: 7px;
}
[dir="rtl"] .item_modified.pull-right {
  float: left !important;
  float: left;
}
.item_buttons {
  line-height: 1em;
  margin-left: -5px;
}
.item_buttons .btn,
.item_buttons .btn-group,
.item_buttons .input-group {
  float: left;
}
.item_buttons > .btn,
.item_buttons > .btn-group,
.item_buttons > .input-group {
  margin-left: 5px;
}
.item_buttons .btn {
  min-width: 13ex;
}
.item_buttons .running-indicator {
  padding-top: 4px;
  color: #5cb85c;
}
.item_buttons .kernel-name {
  padding-top: 4px;
  color: #5bc0de;
  margin-right: 7px;
  float: left;
}
[dir="rtl"] .item_buttons.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .item_buttons .kernel-name {
  margin-left: 7px;
  float: right;
}
.toolbar_info {
  height: 24px;
  line-height: 24px;
}
.list_item input:not([type=checkbox]) {
  padding-top: 3px;
  padding-bottom: 3px;
  height: 22px;
  line-height: 14px;
  margin: 0px;
}
.highlight_text {
  color: blue;
}
#project_name {
  display: inline-block;
  padding-left: 7px;
  margin-left: -2px;
}
#project_name > .breadcrumb {
  padding: 0px;
  margin-bottom: 0px;
  background-color: transparent;
  font-weight: bold;
}
.sort_button {
  display: inline-block;
  padding-left: 7px;
}
[dir="rtl"] .sort_button.pull-right {
  float: left !important;
  float: left;
}
#tree-selector {
  padding-right: 0px;
}
#button-select-all {
  min-width: 50px;
}
[dir="rtl"] #button-select-all.btn {
  float: right ;
}
#select-all {
  margin-left: 7px;
  margin-right: 2px;
  margin-top: 2px;
  height: 16px;
}
[dir="rtl"] #select-all.pull-left {
  float: right !important;
  float: right;
}
.menu_icon {
  margin-right: 2px;
}
.tab-content .row {
  margin-left: 0px;
  margin-right: 0px;
}
.folder_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f114";
}
.folder_icon:before.fa-pull-left {
  margin-right: .3em;
}
.folder_icon:before.fa-pull-right {
  margin-left: .3em;
}
.folder_icon:before.pull-left {
  margin-right: .3em;
}
.folder_icon:before.pull-right {
  margin-left: .3em;
}
.notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
}
.notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.notebook_icon:before.pull-left {
  margin-right: .3em;
}
.notebook_icon:before.pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f02d";
  position: relative;
  top: -1px;
  color: #5cb85c;
}
.running_notebook_icon:before.fa-pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.fa-pull-right {
  margin-left: .3em;
}
.running_notebook_icon:before.pull-left {
  margin-right: .3em;
}
.running_notebook_icon:before.pull-right {
  margin-left: .3em;
}
.file_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f016";
  position: relative;
  top: -2px;
}
.file_icon:before.fa-pull-left {
  margin-right: .3em;
}
.file_icon:before.fa-pull-right {
  margin-left: .3em;
}
.file_icon:before.pull-left {
  margin-right: .3em;
}
.file_icon:before.pull-right {
  margin-left: .3em;
}
#notebook_toolbar .pull-right {
  padding-top: 0px;
  margin-right: -1px;
}
ul#new-menu {
  left: auto;
  right: 0;
}
#new-menu .dropdown-header {
  font-size: 10px;
  border-bottom: 1px solid #e5e5e5;
  padding: 0 0 3px;
  margin: -3px 20px 0;
}
.kernel-menu-icon {
  padding-right: 12px;
  width: 24px;
  content: "\f096";
}
.kernel-menu-icon:before {
  content: "\f096";
}
.kernel-menu-icon-current:before {
  content: "\f00c";
}
#tab_content {
  padding-top: 20px;
}
#running .panel-group .panel {
  margin-top: 3px;
  margin-bottom: 1em;
}
#running .panel-group .panel .panel-heading {
  background-color: #EEE;
  padding-top: 4px;
  padding-bottom: 4px;
  padding-left: 7px;
  padding-right: 7px;
  line-height: 22px;
}
#running .panel-group .panel .panel-heading a:focus,
#running .panel-group .panel .panel-heading a:hover {
  text-decoration: none;
}
#running .panel-group .panel .panel-body {
  padding: 0px;
}
#running .panel-group .panel .panel-body .list_container {
  margin-top: 0px;
  margin-bottom: 0px;
  border: 0px;
  border-radius: 0px;
}
#running .panel-group .panel .panel-body .list_container .list_item {
  border-bottom: 1px solid #ddd;
}
#running .panel-group .panel .panel-body .list_container .list_item:last-child {
  border-bottom: 0px;
}
.delete-button {
  display: none;
}
.duplicate-button {
  display: none;
}
.rename-button {
  display: none;
}
.move-button {
  display: none;
}
.download-button {
  display: none;
}
.shutdown-button {
  display: none;
}
.dynamic-instructions {
  display: inline-block;
  padding-top: 4px;
}
/*!
*
* IPython text editor webapp
*
*/
.selected-keymap i.fa {
  padding: 0px 5px;
}
.selected-keymap i.fa:before {
  content: "\f00c";
}
#mode-menu {
  overflow: auto;
  max-height: 20em;
}
.edit_app #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.edit_app #menubar .navbar {
  /* Use a negative 1 bottom margin, so the border overlaps the border of the
    header */
  margin-bottom: -1px;
}
.dirty-indicator {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator.pull-left {
  margin-right: .3em;
}
.dirty-indicator.pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-dirty.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-dirty.pull-left {
  margin-right: .3em;
}
.dirty-indicator-dirty.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  width: 20px;
}
.dirty-indicator-clean.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean.pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f00c";
}
.dirty-indicator-clean:before.fa-pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.fa-pull-right {
  margin-left: .3em;
}
.dirty-indicator-clean:before.pull-left {
  margin-right: .3em;
}
.dirty-indicator-clean:before.pull-right {
  margin-left: .3em;
}
#filename {
  font-size: 16pt;
  display: table;
  padding: 0px 5px;
}
#current-mode {
  padding-left: 5px;
  padding-right: 5px;
}
#texteditor-backdrop {
  padding-top: 20px;
  padding-bottom: 20px;
}
@media not print {
  #texteditor-backdrop {
    background-color: #EEE;
  }
}
@media print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container .CodeMirror-gutter,
  #texteditor-backdrop #texteditor-container .CodeMirror-gutters {
    background-color: #fff;
  }
}
@media not print {
  #texteditor-backdrop #texteditor-container {
    padding: 0px;
    background-color: #fff;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
.CodeMirror-dialog {
  background-color: #fff;
}
/*!
*
* IPython notebook
*
*/
/* CSS font colors for translated ANSI escape sequences */
/* The color values are a mix of
   http://www.xcolors.net/dl/baskerville-ivorylight and
   http://www.xcolors.net/dl/euphrasia */
.ansi-black-fg {
  color: #3E424D;
}
.ansi-black-bg {
  background-color: #3E424D;
}
.ansi-black-intense-fg {
  color: #282C36;
}
.ansi-black-intense-bg {
  background-color: #282C36;
}
.ansi-red-fg {
  color: #E75C58;
}
.ansi-red-bg {
  background-color: #E75C58;
}
.ansi-red-intense-fg {
  color: #B22B31;
}
.ansi-red-intense-bg {
  background-color: #B22B31;
}
.ansi-green-fg {
  color: #00A250;
}
.ansi-green-bg {
  background-color: #00A250;
}
.ansi-green-intense-fg {
  color: #007427;
}
.ansi-green-intense-bg {
  background-color: #007427;
}
.ansi-yellow-fg {
  color: #DDB62B;
}
.ansi-yellow-bg {
  background-color: #DDB62B;
}
.ansi-yellow-intense-fg {
  color: #B27D12;
}
.ansi-yellow-intense-bg {
  background-color: #B27D12;
}
.ansi-blue-fg {
  color: #208FFB;
}
.ansi-blue-bg {
  background-color: #208FFB;
}
.ansi-blue-intense-fg {
  color: #0065CA;
}
.ansi-blue-intense-bg {
  background-color: #0065CA;
}
.ansi-magenta-fg {
  color: #D160C4;
}
.ansi-magenta-bg {
  background-color: #D160C4;
}
.ansi-magenta-intense-fg {
  color: #A03196;
}
.ansi-magenta-intense-bg {
  background-color: #A03196;
}
.ansi-cyan-fg {
  color: #60C6C8;
}
.ansi-cyan-bg {
  background-color: #60C6C8;
}
.ansi-cyan-intense-fg {
  color: #258F8F;
}
.ansi-cyan-intense-bg {
  background-color: #258F8F;
}
.ansi-white-fg {
  color: #C5C1B4;
}
.ansi-white-bg {
  background-color: #C5C1B4;
}
.ansi-white-intense-fg {
  color: #A1A6B2;
}
.ansi-white-intense-bg {
  background-color: #A1A6B2;
}
.ansi-default-inverse-fg {
  color: #FFFFFF;
}
.ansi-default-inverse-bg {
  background-color: #000000;
}
.ansi-bold {
  font-weight: bold;
}
.ansi-underline {
  text-decoration: underline;
}
/* The following styles are deprecated an will be removed in a future version */
.ansibold {
  font-weight: bold;
}
.ansi-inverse {
  outline: 0.5px dotted;
}
/* use dark versions for foreground, to improve visibility */
.ansiblack {
  color: black;
}
.ansired {
  color: darkred;
}
.ansigreen {
  color: darkgreen;
}
.ansiyellow {
  color: #c4a000;
}
.ansiblue {
  color: darkblue;
}
.ansipurple {
  color: darkviolet;
}
.ansicyan {
  color: steelblue;
}
.ansigray {
  color: gray;
}
/* and light for background, for the same reason */
.ansibgblack {
  background-color: black;
}
.ansibgred {
  background-color: red;
}
.ansibggreen {
  background-color: green;
}
.ansibgyellow {
  background-color: yellow;
}
.ansibgblue {
  background-color: blue;
}
.ansibgpurple {
  background-color: magenta;
}
.ansibgcyan {
  background-color: cyan;
}
.ansibggray {
  background-color: gray;
}
div.cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  border-radius: 2px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  border-width: 1px;
  border-style: solid;
  border-color: transparent;
  width: 100%;
  padding: 5px;
  /* This acts as a spacer between cells, that is outside the border */
  margin: 0px;
  outline: none;
  position: relative;
  overflow: visible;
}
div.cell:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: transparent;
}
div.cell.jupyter-soft-selected {
  border-left-color: #E3F2FD;
  border-left-width: 1px;
  padding-left: 5px;
  border-right-color: #E3F2FD;
  border-right-width: 1px;
  background: #E3F2FD;
}
@media print {
  div.cell.jupyter-soft-selected {
    border-color: transparent;
  }
}
div.cell.selected,
div.cell.selected.jupyter-soft-selected {
  border-color: #ababab;
}
div.cell.selected:before,
div.cell.selected.jupyter-soft-selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #42A5F5;
}
@media print {
  div.cell.selected,
  div.cell.selected.jupyter-soft-selected {
    border-color: transparent;
  }
}
.edit_mode div.cell.selected {
  border-color: #66BB6A;
}
.edit_mode div.cell.selected:before {
  position: absolute;
  display: block;
  top: -1px;
  left: -1px;
  width: 5px;
  height: calc(100% +  2px);
  content: '';
  background: #66BB6A;
}
@media print {
  .edit_mode div.cell.selected {
    border-color: transparent;
  }
}
.prompt {
  /* This needs to be wide enough for 3 digit prompt numbers: In[100]: */
  min-width: 14ex;
  /* This padding is tuned to match the padding on the CodeMirror editor. */
  padding: 0.4em;
  margin: 0px;
  font-family: monospace;
  text-align: right;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
  /* Don't highlight prompt number selection */
  -webkit-touch-callout: none;
  -webkit-user-select: none;
  -khtml-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  /* Use default cursor */
  cursor: default;
}
@media (max-width: 540px) {
  .prompt {
    text-align: left;
  }
}
div.inner_cell {
  min-width: 0;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_area {
  border: 1px solid #cfcfcf;
  border-radius: 2px;
  background: #f7f7f7;
  line-height: 1.21429em;
}
/* This is needed so that empty prompt areas can collapse to zero height when there
   is no content in the output_subarea and the prompt. The main purpose of this is
   to make sure that empty JavaScript output_subareas have no height. */
div.prompt:empty {
  padding-top: 0;
  padding-bottom: 0;
}
div.unrecognized_cell {
  padding: 5px 5px 5px 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.unrecognized_cell .inner_cell {
  border-radius: 2px;
  padding: 5px;
  font-weight: bold;
  color: red;
  border: 1px solid #cfcfcf;
  background: #eaeaea;
}
div.unrecognized_cell .inner_cell a {
  color: inherit;
  text-decoration: none;
}
div.unrecognized_cell .inner_cell a:hover {
  color: inherit;
  text-decoration: none;
}
@media (max-width: 540px) {
  div.unrecognized_cell > div.prompt {
    display: none;
  }
}
div.code_cell {
  /* avoid page breaking on code cells when printing */
}
@media print {
  div.code_cell {
    page-break-inside: avoid;
  }
}
/* any special styling for code cells that are currently running goes here */
div.input {
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.input {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
/* input_area and input_prompt must match in top border and margin for alignment */
div.input_prompt {
  color: #303F9F;
  border-top: 1px solid transparent;
}
div.input_area > div.highlight {
  margin: 0.4em;
  border: none;
  padding: 0px;
  background-color: transparent;
}
div.input_area > div.highlight > pre {
  margin: 0px;
  border: none;
  padding: 0px;
  background-color: transparent;
}
/* The following gets added to the <head> if it is detected that the user has a
 * monospace font with inconsistent normal/bold/italic height.  See
 * notebookmain.js.  Such fonts will have keywords vertically offset with
 * respect to the rest of the text.  The user should select a better font.
 * See: https://github.com/ipython/ipython/issues/1503
 *
 * .CodeMirror span {
 *      vertical-align: bottom;
 * }
 */
.CodeMirror {
  line-height: 1.21429em;
  /* Changed from 1em to our global default */
  font-size: 14px;
  height: auto;
  /* Changed to auto to autogrow */
  background: none;
  /* Changed from white to allow our bg to show through */
}
.CodeMirror-scroll {
  /*  The CodeMirror docs are a bit fuzzy on if overflow-y should be hidden or visible.*/
  /*  We have found that if it is visible, vertical scrollbars appear with font size changes.*/
  overflow-y: hidden;
  overflow-x: auto;
}
.CodeMirror-lines {
  /* In CM2, this used to be 0.4em, but in CM3 it went to 4px. We need the em value because */
  /* we have set a different line-height and want this to scale with that. */
  /* Note that this should set vertical padding only, since CodeMirror assumes
       that horizontal padding will be set on CodeMirror pre */
  padding: 0.4em 0;
}
.CodeMirror-linenumber {
  padding: 0 8px 0 4px;
}
.CodeMirror-gutters {
  border-bottom-left-radius: 2px;
  border-top-left-radius: 2px;
}
.CodeMirror pre {
  /* In CM3 this went to 4px from 0 in CM2. This sets horizontal padding only,
    use .CodeMirror-lines for vertical */
  padding: 0 0.4em;
  border: 0;
  border-radius: 0;
}
.CodeMirror-cursor {
  border-left: 1.4px solid black;
}
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .CodeMirror-cursor {
    border-left: 2px solid black;
  }
}
@media screen and (min-width: 4320px) {
  .CodeMirror-cursor {
    border-left: 4px solid black;
  }
}
/*

Original style from softwaremaniacs.org (c) Ivan Sagalaev <Maniac@SoftwareManiacs.Org>
Adapted from GitHub theme

*/
.highlight-base {
  color: #000;
}
.highlight-variable {
  color: #000;
}
.highlight-variable-2 {
  color: #1a1a1a;
}
.highlight-variable-3 {
  color: #333333;
}
.highlight-string {
  color: #BA2121;
}
.highlight-comment {
  color: #408080;
  font-style: italic;
}
.highlight-number {
  color: #080;
}
.highlight-atom {
  color: #88F;
}
.highlight-keyword {
  color: #008000;
  font-weight: bold;
}
.highlight-builtin {
  color: #008000;
}
.highlight-error {
  color: #f00;
}
.highlight-operator {
  color: #AA22FF;
  font-weight: bold;
}
.highlight-meta {
  color: #AA22FF;
}
/* previously not defined, copying from default codemirror */
.highlight-def {
  color: #00f;
}
.highlight-string-2 {
  color: #f50;
}
.highlight-qualifier {
  color: #555;
}
.highlight-bracket {
  color: #997;
}
.highlight-tag {
  color: #170;
}
.highlight-attribute {
  color: #00c;
}
.highlight-header {
  color: blue;
}
.highlight-quote {
  color: #090;
}
.highlight-link {
  color: #00c;
}
/* apply the same style to codemirror */
.cm-s-ipython span.cm-keyword {
  color: #008000;
  font-weight: bold;
}
.cm-s-ipython span.cm-atom {
  color: #88F;
}
.cm-s-ipython span.cm-number {
  color: #080;
}
.cm-s-ipython span.cm-def {
  color: #00f;
}
.cm-s-ipython span.cm-variable {
  color: #000;
}
.cm-s-ipython span.cm-operator {
  color: #AA22FF;
  font-weight: bold;
}
.cm-s-ipython span.cm-variable-2 {
  color: #1a1a1a;
}
.cm-s-ipython span.cm-variable-3 {
  color: #333333;
}
.cm-s-ipython span.cm-comment {
  color: #408080;
  font-style: italic;
}
.cm-s-ipython span.cm-string {
  color: #BA2121;
}
.cm-s-ipython span.cm-string-2 {
  color: #f50;
}
.cm-s-ipython span.cm-meta {
  color: #AA22FF;
}
.cm-s-ipython span.cm-qualifier {
  color: #555;
}
.cm-s-ipython span.cm-builtin {
  color: #008000;
}
.cm-s-ipython span.cm-bracket {
  color: #997;
}
.cm-s-ipython span.cm-tag {
  color: #170;
}
.cm-s-ipython span.cm-attribute {
  color: #00c;
}
.cm-s-ipython span.cm-header {
  color: blue;
}
.cm-s-ipython span.cm-quote {
  color: #090;
}
.cm-s-ipython span.cm-link {
  color: #00c;
}
.cm-s-ipython span.cm-error {
  color: #f00;
}
.cm-s-ipython span.cm-tab {
  background: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADAAAAAMCAYAAAAkuj5RAAAAAXNSR0IArs4c6QAAAGFJREFUSMft1LsRQFAQheHPowAKoACx3IgEKtaEHujDjORSgWTH/ZOdnZOcM/sgk/kFFWY0qV8foQwS4MKBCS3qR6ixBJvElOobYAtivseIE120FaowJPN75GMu8j/LfMwNjh4HUpwg4LUAAAAASUVORK5CYII=);
  background-position: right;
  background-repeat: no-repeat;
}
div.output_wrapper {
  /* this position must be relative to enable descendents to be absolute within it */
  position: relative;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
  z-index: 1;
}
/* class for the output area when it should be height-limited */
div.output_scroll {
  /* ideally, this would be max-height, but FF barfs all over that */
  height: 24em;
  /* FF needs this *and the wrapper* to specify full width, or it will shrinkwrap */
  width: 100%;
  overflow: auto;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.8);
  display: block;
}
/* output div while it is collapsed */
div.output_collapsed {
  margin: 0px;
  padding: 0px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
div.out_prompt_overlay {
  height: 100%;
  padding: 0px 0.4em;
  position: absolute;
  border-radius: 2px;
}
div.out_prompt_overlay:hover {
  /* use inner shadow to get border that is computed the same on WebKit/FF */
  -webkit-box-shadow: inset 0 0 1px #000;
  box-shadow: inset 0 0 1px #000;
  background: rgba(240, 240, 240, 0.5);
}
div.output_prompt {
  color: #D84315;
}
/* This class is the outer container of all output sections. */
div.output_area {
  padding: 0px;
  page-break-inside: avoid;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
div.output_area .MathJax_Display {
  text-align: left !important;
}
div.output_area .rendered_html table {
  margin-left: 0;
  margin-right: 0;
}
div.output_area .rendered_html img {
  margin-left: 0;
  margin-right: 0;
}
div.output_area img,
div.output_area svg {
  max-width: 100%;
  height: auto;
}
div.output_area img.unconfined,
div.output_area svg.unconfined {
  max-width: none;
}
div.output_area .mglyph > img {
  max-width: none;
}
/* This is needed to protect the pre formating from global settings such
   as that of bootstrap */
.output {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: vertical;
  -moz-box-align: stretch;
  display: box;
  box-orient: vertical;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: column;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.output_area {
    /* Old browsers */
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-box-align: stretch;
    display: -moz-box;
    -moz-box-orient: vertical;
    -moz-box-align: stretch;
    display: box;
    box-orient: vertical;
    box-align: stretch;
    /* Modern browsers */
    display: flex;
    flex-direction: column;
    align-items: stretch;
  }
}
div.output_area pre {
  margin: 0;
  padding: 1px 0 1px 0;
  border: 0;
  vertical-align: baseline;
  color: black;
  background-color: transparent;
  border-radius: 0;
}
/* This class is for the output subarea inside the output_area and after
   the prompt div. */
div.output_subarea {
  overflow-x: auto;
  padding: 0.4em;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
  max-width: calc(100% - 14ex);
}
div.output_scroll div.output_subarea {
  overflow-x: visible;
}
/* The rest of the output_* classes are for special styling of the different
   output types */
/* all text output has this class: */
div.output_text {
  text-align: left;
  color: #000;
  /* This has to match that of the the CodeMirror class line-height below */
  line-height: 1.21429em;
}
/* stdout/stderr are 'text' as well as 'stream', but execute_result/error are *not* streams */
div.output_stderr {
  background: #fdd;
  /* very light red background for stderr */
}
div.output_latex {
  text-align: left;
}
/* Empty output_javascript divs should have no height */
div.output_javascript:empty {
  padding: 0;
}
.js-error {
  color: darkred;
}
/* raw_input styles */
div.raw_input_container {
  line-height: 1.21429em;
  padding-top: 5px;
}
pre.raw_input_prompt {
  /* nothing needed here. */
}
input.raw_input {
  font-family: monospace;
  font-size: inherit;
  color: inherit;
  width: auto;
  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;
  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0em 0.25em;
  margin: 0em 0.25em;
}
input.raw_input:focus {
  box-shadow: none;
}
p.p-space {
  margin-bottom: 10px;
}
div.output_unrecognized {
  padding: 5px;
  font-weight: bold;
  color: red;
}
div.output_unrecognized a {
  color: inherit;
  text-decoration: none;
}
div.output_unrecognized a:hover {
  color: inherit;
  text-decoration: none;
}
.rendered_html {
  color: #000;
  /* any extras will just be numbers: */
}
.rendered_html em {
  font-style: italic;
}
.rendered_html strong {
  font-weight: bold;
}
.rendered_html u {
  text-decoration: underline;
}
.rendered_html :link {
  text-decoration: underline;
}
.rendered_html :visited {
  text-decoration: underline;
}
.rendered_html h1 {
  font-size: 185.7%;
  margin: 1.08em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h2 {
  font-size: 157.1%;
  margin: 1.27em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h3 {
  font-size: 128.6%;
  margin: 1.55em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h4 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
}
.rendered_html h5 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h6 {
  font-size: 100%;
  margin: 2em 0 0 0;
  font-weight: bold;
  line-height: 1.0;
  font-style: italic;
}
.rendered_html h1:first-child {
  margin-top: 0.538em;
}
.rendered_html h2:first-child {
  margin-top: 0.636em;
}
.rendered_html h3:first-child {
  margin-top: 0.777em;
}
.rendered_html h4:first-child {
  margin-top: 1em;
}
.rendered_html h5:first-child {
  margin-top: 1em;
}
.rendered_html h6:first-child {
  margin-top: 1em;
}
.rendered_html ul:not(.list-inline),
.rendered_html ol:not(.list-inline) {
  padding-left: 2em;
}
.rendered_html ul {
  list-style: disc;
}
.rendered_html ul ul {
  list-style: square;
  margin-top: 0;
}
.rendered_html ul ul ul {
  list-style: circle;
}
.rendered_html ol {
  list-style: decimal;
}
.rendered_html ol ol {
  list-style: upper-alpha;
  margin-top: 0;
}
.rendered_html ol ol ol {
  list-style: lower-alpha;
}
.rendered_html ol ol ol ol {
  list-style: lower-roman;
}
.rendered_html ol ol ol ol ol {
  list-style: decimal;
}
.rendered_html * + ul {
  margin-top: 1em;
}
.rendered_html * + ol {
  margin-top: 1em;
}
.rendered_html hr {
  color: black;
  background-color: black;
}
.rendered_html pre {
  margin: 1em 2em;
  padding: 0px;
  background-color: #fff;
}
.rendered_html code {
  background-color: #eff0f1;
}
.rendered_html p code {
  padding: 1px 5px;
}
.rendered_html pre code {
  background-color: #fff;
}
.rendered_html pre,
.rendered_html code {
  border: 0;
  color: #000;
  font-size: 100%;
}
.rendered_html blockquote {
  margin: 1em 2em;
}
.rendered_html table {
  margin-left: auto;
  margin-right: auto;
  border: none;
  border-collapse: collapse;
  border-spacing: 0;
  color: black;
  font-size: 12px;
  table-layout: fixed;
}
.rendered_html thead {
  border-bottom: 1px solid black;
  vertical-align: bottom;
}
.rendered_html tr,
.rendered_html th,
.rendered_html td {
  text-align: right;
  vertical-align: middle;
  padding: 0.5em 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}
.rendered_html th {
  font-weight: bold;
}
.rendered_html tbody tr:nth-child(odd) {
  background: #f5f5f5;
}
.rendered_html tbody tr:hover {
  background: rgba(66, 165, 245, 0.2);
}
.rendered_html * + table {
  margin-top: 1em;
}
.rendered_html p {
  text-align: left;
}
.rendered_html * + p {
  margin-top: 1em;
}
.rendered_html img {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
.rendered_html * + img {
  margin-top: 1em;
}
.rendered_html img,
.rendered_html svg {
  max-width: 100%;
  height: auto;
}
.rendered_html img.unconfined,
.rendered_html svg.unconfined {
  max-width: none;
}
.rendered_html .alert {
  margin-bottom: initial;
}
.rendered_html * + .alert {
  margin-top: 1em;
}
[dir="rtl"] .rendered_html p {
  text-align: right;
}
div.text_cell {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
}
@media (max-width: 540px) {
  div.text_cell > div.prompt {
    display: none;
  }
}
div.text_cell_render {
  /*font-family: "Helvetica Neue", Arial, Helvetica, Geneva, sans-serif;*/
  outline: none;
  resize: none;
  width: inherit;
  border-style: none;
  padding: 0.5em 0.5em 0.5em 0.4em;
  color: #000;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
a.anchor-link:link {
  text-decoration: none;
  padding: 0px 20px;
  visibility: hidden;
}
h1:hover .anchor-link,
h2:hover .anchor-link,
h3:hover .anchor-link,
h4:hover .anchor-link,
h5:hover .anchor-link,
h6:hover .anchor-link {
  visibility: visible;
}
.text_cell.rendered .input_area {
  display: none;
}
.text_cell.rendered .rendered_html {
  overflow-x: auto;
  overflow-y: hidden;
}
.text_cell.rendered .rendered_html tr,
.text_cell.rendered .rendered_html th,
.text_cell.rendered .rendered_html td {
  max-width: none;
}
.text_cell.unrendered .text_cell_render {
  display: none;
}
.text_cell .dropzone .input_area {
  border: 2px dashed #bababa;
  margin: -1px;
}
.cm-header-1,
.cm-header-2,
.cm-header-3,
.cm-header-4,
.cm-header-5,
.cm-header-6 {
  font-weight: bold;
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
.cm-header-1 {
  font-size: 185.7%;
}
.cm-header-2 {
  font-size: 157.1%;
}
.cm-header-3 {
  font-size: 128.6%;
}
.cm-header-4 {
  font-size: 110%;
}
.cm-header-5 {
  font-size: 100%;
  font-style: italic;
}
.cm-header-6 {
  font-size: 100%;
  font-style: italic;
}
/*!
*
* IPython notebook webapp
*
*/
@media (max-width: 767px) {
  .notebook_app {
    padding-left: 0px;
    padding-right: 0px;
  }
}
#ipython-main-app {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook_panel {
  margin: 0px;
  padding: 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  height: 100%;
}
div#notebook {
  font-size: 14px;
  line-height: 20px;
  overflow-y: hidden;
  overflow-x: auto;
  width: 100%;
  /* This spaces the page away from the edge of the notebook area */
  padding-top: 20px;
  margin: 0px;
  outline: none;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  min-height: 100%;
}
@media not print {
  #notebook-container {
    padding: 15px;
    background-color: #fff;
    min-height: 0;
    -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
    box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  }
}
@media print {
  #notebook-container {
    width: 100%;
  }
}
div.ui-widget-content {
  border: 1px solid #ababab;
  outline: none;
}
pre.dialog {
  background-color: #f7f7f7;
  border: 1px solid #ddd;
  border-radius: 2px;
  padding: 0.4em;
  padding-left: 2em;
}
p.dialog {
  padding: 0.2em;
}
/* Word-wrap output correctly.  This is the CSS3 spelling, though Firefox seems
   to not honor it correctly.  Webkit browsers (Chrome, rekonq, Safari) do.
 */
pre,
code,
kbd,
samp {
  white-space: pre-wrap;
}
#fonttest {
  font-family: monospace;
}
p {
  margin-bottom: 0;
}
.end_space {
  min-height: 100px;
  transition: height .2s ease;
}
.notebook_app > #header {
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
@media not print {
  .notebook_app {
    background-color: #EEE;
  }
}
kbd {
  border-style: solid;
  border-width: 1px;
  box-shadow: none;
  margin: 2px;
  padding-left: 2px;
  padding-right: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
.jupyter-keybindings {
  padding: 1px;
  line-height: 24px;
  border-bottom: 1px solid gray;
}
.jupyter-keybindings input {
  margin: 0;
  padding: 0;
  border: none;
}
.jupyter-keybindings i {
  padding: 6px;
}
.well code {
  background-color: #ffffff;
  border-color: #ababab;
  border-width: 1px;
  border-style: solid;
  padding: 2px;
  padding-top: 1px;
  padding-bottom: 1px;
}
/* CSS for the cell toolbar */
.celltoolbar {
  border: thin solid #CFCFCF;
  border-bottom: none;
  background: #EEE;
  border-radius: 2px 2px 0px 0px;
  width: 100%;
  height: 29px;
  padding-right: 4px;
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  /* Old browsers */
  -webkit-box-pack: end;
  -moz-box-pack: end;
  box-pack: end;
  /* Modern browsers */
  justify-content: flex-end;
  display: -webkit-flex;
}
@media print {
  .celltoolbar {
    display: none;
  }
}
.ctb_hideshow {
  display: none;
  vertical-align: bottom;
}
/* ctb_show is added to the ctb_hideshow div to show the cell toolbar.
   Cell toolbars are only shown when the ctb_global_show class is also set.
*/
.ctb_global_show .ctb_show.ctb_hideshow {
  display: block;
}
.ctb_global_show .ctb_show + .input_area,
.ctb_global_show .ctb_show + div.text_cell_input,
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border-top-right-radius: 0px;
  border-top-left-radius: 0px;
}
.ctb_global_show .ctb_show ~ div.text_cell_render {
  border: 1px solid #cfcfcf;
}
.celltoolbar {
  font-size: 87%;
  padding-top: 3px;
}
.celltoolbar select {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  width: inherit;
  font-size: inherit;
  height: 22px;
  padding: 0px;
  display: inline-block;
}
.celltoolbar select:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.celltoolbar select::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.celltoolbar select:-ms-input-placeholder {
  color: #999;
}
.celltoolbar select::-webkit-input-placeholder {
  color: #999;
}
.celltoolbar select::-ms-expand {
  border: 0;
  background-color: transparent;
}
.celltoolbar select[disabled],
.celltoolbar select[readonly],
fieldset[disabled] .celltoolbar select {
  background-color: #eeeeee;
  opacity: 1;
}
.celltoolbar select[disabled],
fieldset[disabled] .celltoolbar select {
  cursor: not-allowed;
}
textarea.celltoolbar select {
  height: auto;
}
select.celltoolbar select {
  height: 30px;
  line-height: 30px;
}
textarea.celltoolbar select,
select[multiple].celltoolbar select {
  height: auto;
}
.celltoolbar label {
  margin-left: 5px;
  margin-right: 5px;
}
.tags_button_container {
  width: 100%;
  display: flex;
}
.tag-container {
  display: flex;
  flex-direction: row;
  flex-grow: 1;
  overflow: hidden;
  position: relative;
}
.tag-container > * {
  margin: 0 4px;
}
.remove-tag-btn {
  margin-left: 4px;
}
.tags-input {
  display: flex;
}
.cell-tag:last-child:after {
  content: "";
  position: absolute;
  right: 0;
  width: 40px;
  height: 100%;
  /* Fade to background color of cell toolbar */
  background: linear-gradient(to right, rgba(0, 0, 0, 0), #EEE);
}
.tags-input > * {
  margin-left: 4px;
}
.cell-tag,
.tags-input input,
.tags-input button {
  display: block;
  width: 100%;
  height: 32px;
  padding: 6px 12px;
  font-size: 13px;
  line-height: 1.42857143;
  color: #555555;
  background-color: #fff;
  background-image: none;
  border: 1px solid #ccc;
  border-radius: 2px;
  -webkit-box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  box-shadow: inset 0 1px 1px rgba(0, 0, 0, 0.075);
  -webkit-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  -o-transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  transition: border-color ease-in-out .15s, box-shadow ease-in-out .15s;
  height: 30px;
  padding: 5px 10px;
  font-size: 12px;
  line-height: 1.5;
  border-radius: 1px;
  box-shadow: none;
  width: inherit;
  font-size: inherit;
  height: 22px;
  line-height: 22px;
  padding: 0px 4px;
  display: inline-block;
}
.cell-tag:focus,
.tags-input input:focus,
.tags-input button:focus {
  border-color: #66afe9;
  outline: 0;
  -webkit-box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
  box-shadow: inset 0 1px 1px rgba(0,0,0,.075), 0 0 8px rgba(102, 175, 233, 0.6);
}
.cell-tag::-moz-placeholder,
.tags-input input::-moz-placeholder,
.tags-input button::-moz-placeholder {
  color: #999;
  opacity: 1;
}
.cell-tag:-ms-input-placeholder,
.tags-input input:-ms-input-placeholder,
.tags-input button:-ms-input-placeholder {
  color: #999;
}
.cell-tag::-webkit-input-placeholder,
.tags-input input::-webkit-input-placeholder,
.tags-input button::-webkit-input-placeholder {
  color: #999;
}
.cell-tag::-ms-expand,
.tags-input input::-ms-expand,
.tags-input button::-ms-expand {
  border: 0;
  background-color: transparent;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
.cell-tag[readonly],
.tags-input input[readonly],
.tags-input button[readonly],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  background-color: #eeeeee;
  opacity: 1;
}
.cell-tag[disabled],
.tags-input input[disabled],
.tags-input button[disabled],
fieldset[disabled] .cell-tag,
fieldset[disabled] .tags-input input,
fieldset[disabled] .tags-input button {
  cursor: not-allowed;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button {
  height: auto;
}
select.cell-tag,
select.tags-input input,
select.tags-input button {
  height: 30px;
  line-height: 30px;
}
textarea.cell-tag,
textarea.tags-input input,
textarea.tags-input button,
select[multiple].cell-tag,
select[multiple].tags-input input,
select[multiple].tags-input button {
  height: auto;
}
.cell-tag,
.tags-input button {
  padding: 0px 4px;
}
.cell-tag {
  background-color: #fff;
  white-space: nowrap;
}
.tags-input input[type=text]:focus {
  outline: none;
  box-shadow: none;
  border-color: #ccc;
}
.completions {
  position: absolute;
  z-index: 110;
  overflow: hidden;
  border: 1px solid #ababab;
  border-radius: 2px;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  line-height: 1;
}
.completions select {
  background: white;
  outline: none;
  border: none;
  padding: 0px;
  margin: 0px;
  overflow: auto;
  font-family: monospace;
  font-size: 110%;
  color: #000;
  width: auto;
}
.completions select option.context {
  color: #286090;
}
#kernel_logo_widget .current_kernel_logo {
  display: none;
  margin-top: -1px;
  margin-bottom: -1px;
  width: 32px;
  height: 32px;
}
[dir="rtl"] #kernel_logo_widget {
  float: left !important;
  float: left;
}
.modal .modal-body .move-path {
  display: flex;
  flex-direction: row;
  justify-content: space;
  align-items: center;
}
.modal .modal-body .move-path .server-root {
  padding-right: 20px;
}
.modal .modal-body .move-path .path-input {
  flex: 1;
}
#menubar {
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  margin-top: 1px;
}
#menubar .navbar {
  border-top: 1px;
  border-radius: 0px 0px 2px 2px;
  margin-bottom: 0px;
}
#menubar .navbar-toggle {
  float: left;
  padding-top: 7px;
  padding-bottom: 7px;
  border: none;
}
#menubar .navbar-collapse {
  clear: left;
}
[dir="rtl"] #menubar .navbar-toggle {
  float: right;
}
[dir="rtl"] #menubar .navbar-collapse {
  clear: right;
}
[dir="rtl"] #menubar .navbar-nav {
  float: right;
}
[dir="rtl"] #menubar .nav {
  padding-right: 0px;
}
[dir="rtl"] #menubar .navbar-nav > li {
  float: right;
}
[dir="rtl"] #menubar .navbar-right {
  float: left !important;
}
[dir="rtl"] ul.dropdown-menu {
  text-align: right;
  left: auto;
}
[dir="rtl"] ul#new-menu.dropdown-menu {
  right: auto;
  left: 0;
}
.nav-wrapper {
  border-bottom: 1px solid #e7e7e7;
}
i.menu-icon {
  padding-top: 4px;
}
[dir="rtl"] i.menu-icon.pull-right {
  float: left !important;
  float: left;
}
ul#help_menu li a {
  overflow: hidden;
  padding-right: 2.2em;
}
ul#help_menu li a i {
  margin-right: -1.2em;
}
[dir="rtl"] ul#help_menu li a {
  padding-left: 2.2em;
}
[dir="rtl"] ul#help_menu li a i {
  margin-right: 0;
  margin-left: -1.2em;
}
[dir="rtl"] ul#help_menu li a i.pull-right {
  float: left !important;
  float: left;
}
.dropdown-submenu {
  position: relative;
}
.dropdown-submenu > .dropdown-menu {
  top: 0;
  left: 100%;
  margin-top: -6px;
  margin-left: -1px;
}
[dir="rtl"] .dropdown-submenu > .dropdown-menu {
  right: 100%;
  margin-right: -1px;
}
.dropdown-submenu:hover > .dropdown-menu {
  display: block;
}
.dropdown-submenu > a:after {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: block;
  content: "\f0da";
  float: right;
  color: #333333;
  margin-top: 2px;
  margin-right: -10px;
}
.dropdown-submenu > a:after.fa-pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.fa-pull-right {
  margin-left: .3em;
}
.dropdown-submenu > a:after.pull-left {
  margin-right: .3em;
}
.dropdown-submenu > a:after.pull-right {
  margin-left: .3em;
}
[dir="rtl"] .dropdown-submenu > a:after {
  float: left;
  content: "\f0d9";
  margin-right: 0;
  margin-left: -10px;
}
.dropdown-submenu:hover > a:after {
  color: #262626;
}
.dropdown-submenu.pull-left {
  float: none;
}
.dropdown-submenu.pull-left > .dropdown-menu {
  left: -100%;
  margin-left: 10px;
}
#notification_area {
  float: right !important;
  float: right;
  z-index: 10;
}
[dir="rtl"] #notification_area {
  float: left !important;
  float: left;
}
.indicator_area {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] .indicator_area {
  float: left !important;
  float: left;
}
#kernel_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  border-left: 1px solid;
}
#kernel_indicator .kernel_indicator_name {
  padding-left: 5px;
  padding-right: 5px;
}
[dir="rtl"] #kernel_indicator {
  float: left !important;
  float: left;
  border-left: 0;
  border-right: 1px solid;
}
#modal_indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
}
[dir="rtl"] #modal_indicator {
  float: left !important;
  float: left;
}
#readonly-indicator {
  float: right !important;
  float: right;
  color: #777;
  margin-left: 5px;
  margin-right: 5px;
  width: 11px;
  z-index: 10;
  text-align: center;
  width: auto;
  margin-top: 2px;
  margin-bottom: 0px;
  margin-left: 0px;
  margin-right: 0px;
  display: none;
}
.modal_indicator:before {
  width: 1.28571429em;
  text-align: center;
}
.edit_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f040";
}
.edit_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.edit_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.edit_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: ' ';
}
.command_mode .modal_indicator:before.fa-pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.fa-pull-right {
  margin-left: .3em;
}
.command_mode .modal_indicator:before.pull-left {
  margin-right: .3em;
}
.command_mode .modal_indicator:before.pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f10c";
}
.kernel_idle_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_idle_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_idle_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f111";
}
.kernel_busy_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_busy_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_busy_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f1e2";
}
.kernel_dead_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_dead_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_dead_icon:before.pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before {
  display: inline-block;
  font: normal normal normal 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  content: "\f127";
}
.kernel_disconnected_icon:before.fa-pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.fa-pull-right {
  margin-left: .3em;
}
.kernel_disconnected_icon:before.pull-left {
  margin-right: .3em;
}
.kernel_disconnected_icon:before.pull-right {
  margin-left: .3em;
}
.notification_widget {
  color: #777;
  z-index: 10;
  background: rgba(240, 240, 240, 0.5);
  margin-right: 4px;
  color: #333;
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget:focus,
.notification_widget.focus {
  color: #333;
  background-color: #e6e6e6;
  border-color: #8c8c8c;
}
.notification_widget:hover {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  color: #333;
  background-color: #e6e6e6;
  border-color: #adadad;
}
.notification_widget:active:hover,
.notification_widget.active:hover,
.open > .dropdown-toggle.notification_widget:hover,
.notification_widget:active:focus,
.notification_widget.active:focus,
.open > .dropdown-toggle.notification_widget:focus,
.notification_widget:active.focus,
.notification_widget.active.focus,
.open > .dropdown-toggle.notification_widget.focus {
  color: #333;
  background-color: #d4d4d4;
  border-color: #8c8c8c;
}
.notification_widget:active,
.notification_widget.active,
.open > .dropdown-toggle.notification_widget {
  background-image: none;
}
.notification_widget.disabled:hover,
.notification_widget[disabled]:hover,
fieldset[disabled] .notification_widget:hover,
.notification_widget.disabled:focus,
.notification_widget[disabled]:focus,
fieldset[disabled] .notification_widget:focus,
.notification_widget.disabled.focus,
.notification_widget[disabled].focus,
fieldset[disabled] .notification_widget.focus {
  background-color: #fff;
  border-color: #ccc;
}
.notification_widget .badge {
  color: #fff;
  background-color: #333;
}
.notification_widget.warning {
  color: #fff;
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning:focus,
.notification_widget.warning.focus {
  color: #fff;
  background-color: #ec971f;
  border-color: #985f0d;
}
.notification_widget.warning:hover {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  color: #fff;
  background-color: #ec971f;
  border-color: #d58512;
}
.notification_widget.warning:active:hover,
.notification_widget.warning.active:hover,
.open > .dropdown-toggle.notification_widget.warning:hover,
.notification_widget.warning:active:focus,
.notification_widget.warning.active:focus,
.open > .dropdown-toggle.notification_widget.warning:focus,
.notification_widget.warning:active.focus,
.notification_widget.warning.active.focus,
.open > .dropdown-toggle.notification_widget.warning.focus {
  color: #fff;
  background-color: #d58512;
  border-color: #985f0d;
}
.notification_widget.warning:active,
.notification_widget.warning.active,
.open > .dropdown-toggle.notification_widget.warning {
  background-image: none;
}
.notification_widget.warning.disabled:hover,
.notification_widget.warning[disabled]:hover,
fieldset[disabled] .notification_widget.warning:hover,
.notification_widget.warning.disabled:focus,
.notification_widget.warning[disabled]:focus,
fieldset[disabled] .notification_widget.warning:focus,
.notification_widget.warning.disabled.focus,
.notification_widget.warning[disabled].focus,
fieldset[disabled] .notification_widget.warning.focus {
  background-color: #f0ad4e;
  border-color: #eea236;
}
.notification_widget.warning .badge {
  color: #f0ad4e;
  background-color: #fff;
}
.notification_widget.success {
  color: #fff;
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success:focus,
.notification_widget.success.focus {
  color: #fff;
  background-color: #449d44;
  border-color: #255625;
}
.notification_widget.success:hover {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  color: #fff;
  background-color: #449d44;
  border-color: #398439;
}
.notification_widget.success:active:hover,
.notification_widget.success.active:hover,
.open > .dropdown-toggle.notification_widget.success:hover,
.notification_widget.success:active:focus,
.notification_widget.success.active:focus,
.open > .dropdown-toggle.notification_widget.success:focus,
.notification_widget.success:active.focus,
.notification_widget.success.active.focus,
.open > .dropdown-toggle.notification_widget.success.focus {
  color: #fff;
  background-color: #398439;
  border-color: #255625;
}
.notification_widget.success:active,
.notification_widget.success.active,
.open > .dropdown-toggle.notification_widget.success {
  background-image: none;
}
.notification_widget.success.disabled:hover,
.notification_widget.success[disabled]:hover,
fieldset[disabled] .notification_widget.success:hover,
.notification_widget.success.disabled:focus,
.notification_widget.success[disabled]:focus,
fieldset[disabled] .notification_widget.success:focus,
.notification_widget.success.disabled.focus,
.notification_widget.success[disabled].focus,
fieldset[disabled] .notification_widget.success.focus {
  background-color: #5cb85c;
  border-color: #4cae4c;
}
.notification_widget.success .badge {
  color: #5cb85c;
  background-color: #fff;
}
.notification_widget.info {
  color: #fff;
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info:focus,
.notification_widget.info.focus {
  color: #fff;
  background-color: #31b0d5;
  border-color: #1b6d85;
}
.notification_widget.info:hover {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  color: #fff;
  background-color: #31b0d5;
  border-color: #269abc;
}
.notification_widget.info:active:hover,
.notification_widget.info.active:hover,
.open > .dropdown-toggle.notification_widget.info:hover,
.notification_widget.info:active:focus,
.notification_widget.info.active:focus,
.open > .dropdown-toggle.notification_widget.info:focus,
.notification_widget.info:active.focus,
.notification_widget.info.active.focus,
.open > .dropdown-toggle.notification_widget.info.focus {
  color: #fff;
  background-color: #269abc;
  border-color: #1b6d85;
}
.notification_widget.info:active,
.notification_widget.info.active,
.open > .dropdown-toggle.notification_widget.info {
  background-image: none;
}
.notification_widget.info.disabled:hover,
.notification_widget.info[disabled]:hover,
fieldset[disabled] .notification_widget.info:hover,
.notification_widget.info.disabled:focus,
.notification_widget.info[disabled]:focus,
fieldset[disabled] .notification_widget.info:focus,
.notification_widget.info.disabled.focus,
.notification_widget.info[disabled].focus,
fieldset[disabled] .notification_widget.info.focus {
  background-color: #5bc0de;
  border-color: #46b8da;
}
.notification_widget.info .badge {
  color: #5bc0de;
  background-color: #fff;
}
.notification_widget.danger {
  color: #fff;
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger:focus,
.notification_widget.danger.focus {
  color: #fff;
  background-color: #c9302c;
  border-color: #761c19;
}
.notification_widget.danger:hover {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  color: #fff;
  background-color: #c9302c;
  border-color: #ac2925;
}
.notification_widget.danger:active:hover,
.notification_widget.danger.active:hover,
.open > .dropdown-toggle.notification_widget.danger:hover,
.notification_widget.danger:active:focus,
.notification_widget.danger.active:focus,
.open > .dropdown-toggle.notification_widget.danger:focus,
.notification_widget.danger:active.focus,
.notification_widget.danger.active.focus,
.open > .dropdown-toggle.notification_widget.danger.focus {
  color: #fff;
  background-color: #ac2925;
  border-color: #761c19;
}
.notification_widget.danger:active,
.notification_widget.danger.active,
.open > .dropdown-toggle.notification_widget.danger {
  background-image: none;
}
.notification_widget.danger.disabled:hover,
.notification_widget.danger[disabled]:hover,
fieldset[disabled] .notification_widget.danger:hover,
.notification_widget.danger.disabled:focus,
.notification_widget.danger[disabled]:focus,
fieldset[disabled] .notification_widget.danger:focus,
.notification_widget.danger.disabled.focus,
.notification_widget.danger[disabled].focus,
fieldset[disabled] .notification_widget.danger.focus {
  background-color: #d9534f;
  border-color: #d43f3a;
}
.notification_widget.danger .badge {
  color: #d9534f;
  background-color: #fff;
}
div#pager {
  background-color: #fff;
  font-size: 14px;
  line-height: 20px;
  overflow: hidden;
  display: none;
  position: fixed;
  bottom: 0px;
  width: 100%;
  max-height: 50%;
  padding-top: 8px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  /* Display over codemirror */
  z-index: 100;
  /* Hack which prevents jquery ui resizable from changing top. */
  top: auto !important;
}
div#pager pre {
  line-height: 1.21429em;
  color: #000;
  background-color: #f7f7f7;
  padding: 0.4em;
}
div#pager #pager-button-area {
  position: absolute;
  top: 8px;
  right: 20px;
}
div#pager #pager-contents {
  position: relative;
  overflow: auto;
  width: 100%;
  height: 100%;
}
div#pager #pager-contents #pager-container {
  position: relative;
  padding: 15px 0px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
div#pager .ui-resizable-handle {
  top: 0px;
  height: 8px;
  background: #f7f7f7;
  border-top: 1px solid #cfcfcf;
  border-bottom: 1px solid #cfcfcf;
  /* This injects handle bars (a short, wide = symbol) for 
        the resize handle. */
}
div#pager .ui-resizable-handle::after {
  content: '';
  top: 2px;
  left: 50%;
  height: 3px;
  width: 30px;
  margin-left: -15px;
  position: absolute;
  border-top: 1px solid #cfcfcf;
}
.quickhelp {
  /* Old browsers */
  display: -webkit-box;
  -webkit-box-orient: horizontal;
  -webkit-box-align: stretch;
  display: -moz-box;
  -moz-box-orient: horizontal;
  -moz-box-align: stretch;
  display: box;
  box-orient: horizontal;
  box-align: stretch;
  /* Modern browsers */
  display: flex;
  flex-direction: row;
  align-items: stretch;
  line-height: 1.8em;
}
.shortcut_key {
  display: inline-block;
  width: 21ex;
  text-align: right;
  font-family: monospace;
}
.shortcut_descr {
  display: inline-block;
  /* Old browsers */
  -webkit-box-flex: 1;
  -moz-box-flex: 1;
  box-flex: 1;
  /* Modern browsers */
  flex: 1;
}
span.save_widget {
  height: 30px;
  margin-top: 4px;
  display: flex;
  justify-content: flex-start;
  align-items: baseline;
  width: 50%;
  flex: 1;
}
span.save_widget span.filename {
  height: 100%;
  line-height: 1em;
  margin-left: 16px;
  border: none;
  font-size: 146.5%;
  text-overflow: ellipsis;
  overflow: hidden;
  white-space: nowrap;
  border-radius: 2px;
}
span.save_widget span.filename:hover {
  background-color: #e6e6e6;
}
[dir="rtl"] span.save_widget.pull-left {
  float: right !important;
  float: right;
}
[dir="rtl"] span.save_widget span.filename {
  margin-left: 0;
  margin-right: 16px;
}
span.checkpoint_status,
span.autosave_status {
  font-size: small;
  white-space: nowrap;
  padding: 0 5px;
}
@media (max-width: 767px) {
  span.save_widget {
    font-size: small;
    padding: 0 0 0 5px;
  }
  span.checkpoint_status,
  span.autosave_status {
    display: none;
  }
}
@media (min-width: 768px) and (max-width: 991px) {
  span.checkpoint_status {
    display: none;
  }
  span.autosave_status {
    font-size: x-small;
  }
}
.toolbar {
  padding: 0px;
  margin-left: -5px;
  margin-top: 2px;
  margin-bottom: 5px;
  box-sizing: border-box;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
}
.toolbar select,
.toolbar label {
  width: auto;
  vertical-align: middle;
  margin-right: 2px;
  margin-bottom: 0px;
  display: inline;
  font-size: 92%;
  margin-left: 0.3em;
  margin-right: 0.3em;
  padding: 0px;
  padding-top: 3px;
}
.toolbar .btn {
  padding: 2px 8px;
}
.toolbar .btn-group {
  margin-top: 0px;
  margin-left: 5px;
}
.toolbar-btn-label {
  margin-left: 6px;
}
#maintoolbar {
  margin-bottom: -3px;
  margin-top: -8px;
  border: 0px;
  min-height: 27px;
  margin-left: 0px;
  padding-top: 11px;
  padding-bottom: 3px;
}
#maintoolbar .navbar-text {
  float: none;
  vertical-align: middle;
  text-align: right;
  margin-left: 5px;
  margin-right: 0px;
  margin-top: 0px;
}
.select-xs {
  height: 24px;
}
[dir="rtl"] .btn-group > .btn,
.btn-group-vertical > .btn {
  float: right;
}
.pulse,
.dropdown-menu > li > a.pulse,
li.pulse > a.dropdown-toggle,
li.pulse.open > a.dropdown-toggle {
  background-color: #F37626;
  color: white;
}
/**
 * Primary styles
 *
 * Author: Jupyter Development Team
 */
/** WARNING IF YOU ARE EDITTING THIS FILE, if this is a .css file, It has a lot
 * of chance of beeing generated from the ../less/[samename].less file, you can
 * try to get back the less file by reverting somme commit in history
 **/
/*
 * We'll try to get something pretty, so we
 * have some strange css to have the scroll bar on
 * the left with fix button on the top right of the tooltip
 */
@-moz-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-webkit-keyframes fadeOut {
  from {
    opacity: 1;
  }
  to {
    opacity: 0;
  }
}
@-moz-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
@-webkit-keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}
/*properties of tooltip after "expand"*/
.bigtooltip {
  overflow: auto;
  height: 200px;
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
}
/*properties of tooltip before "expand"*/
.smalltooltip {
  -webkit-transition-property: height;
  -webkit-transition-duration: 500ms;
  -moz-transition-property: height;
  -moz-transition-duration: 500ms;
  transition-property: height;
  transition-duration: 500ms;
  text-overflow: ellipsis;
  overflow: hidden;
  height: 80px;
}
.tooltipbuttons {
  position: absolute;
  padding-right: 15px;
  top: 0px;
  right: 0px;
}
.tooltiptext {
  /*avoid the button to overlap on some docstring*/
  padding-right: 30px;
}
.ipython_tooltip {
  max-width: 700px;
  /*fade-in animation when inserted*/
  -webkit-animation: fadeOut 400ms;
  -moz-animation: fadeOut 400ms;
  animation: fadeOut 400ms;
  -webkit-animation: fadeIn 400ms;
  -moz-animation: fadeIn 400ms;
  animation: fadeIn 400ms;
  vertical-align: middle;
  background-color: #f7f7f7;
  overflow: visible;
  border: #ababab 1px solid;
  outline: none;
  padding: 3px;
  margin: 0px;
  padding-left: 7px;
  font-family: monospace;
  min-height: 50px;
  -moz-box-shadow: 0px 6px 10px -1px #adadad;
  -webkit-box-shadow: 0px 6px 10px -1px #adadad;
  box-shadow: 0px 6px 10px -1px #adadad;
  border-radius: 2px;
  position: absolute;
  z-index: 1000;
}
.ipython_tooltip a {
  float: right;
}
.ipython_tooltip .tooltiptext pre {
  border: 0;
  border-radius: 0;
  font-size: 100%;
  background-color: #f7f7f7;
}
.pretooltiparrow {
  left: 0px;
  margin: 0px;
  top: -16px;
  width: 40px;
  height: 16px;
  overflow: hidden;
  position: absolute;
}
.pretooltiparrow:before {
  background-color: #f7f7f7;
  border: 1px #ababab solid;
  z-index: 11;
  content: "";
  position: absolute;
  left: 15px;
  top: 10px;
  width: 25px;
  height: 25px;
  -webkit-transform: rotate(45deg);
  -moz-transform: rotate(45deg);
  -ms-transform: rotate(45deg);
  -o-transform: rotate(45deg);
}
ul.typeahead-list i {
  margin-left: -10px;
  width: 18px;
}
[dir="rtl"] ul.typeahead-list i {
  margin-left: 0;
  margin-right: -10px;
}
ul.typeahead-list {
  max-height: 80vh;
  overflow: auto;
}
ul.typeahead-list > li > a {
  /** Firefox bug **/
  /* see https://github.com/jupyter/notebook/issues/559 */
  white-space: normal;
}
ul.typeahead-list  > li > a.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .typeahead-list {
  text-align: right;
}
.cmd-palette .modal-body {
  padding: 7px;
}
.cmd-palette form {
  background: white;
}
.cmd-palette input {
  outline: none;
}
.no-shortcut {
  min-width: 20px;
  color: transparent;
}
[dir="rtl"] .no-shortcut.pull-right {
  float: left !important;
  float: left;
}
[dir="rtl"] .command-shortcut.pull-right {
  float: left !important;
  float: left;
}
.command-shortcut:before {
  content: "(command mode)";
  padding-right: 3px;
  color: #777777;
}
.edit-shortcut:before {
  content: "(edit)";
  padding-right: 3px;
  color: #777777;
}
[dir="rtl"] .edit-shortcut.pull-right {
  float: left !important;
  float: left;
}
#find-and-replace #replace-preview .match,
#find-and-replace #replace-preview .insert {
  background-color: #BBDEFB;
  border-color: #90CAF9;
  border-style: solid;
  border-width: 1px;
  border-radius: 0px;
}
[dir="ltr"] #find-and-replace .input-group-btn + .form-control {
  border-left: none;
}
[dir="rtl"] #find-and-replace .input-group-btn + .form-control {
  border-right: none;
}
#find-and-replace #replace-preview .replace .match {
  background-color: #FFCDD2;
  border-color: #EF9A9A;
  border-radius: 0px;
}
#find-and-replace #replace-preview .replace .insert {
  background-color: #C8E6C9;
  border-color: #A5D6A7;
  border-radius: 0px;
}
#find-and-replace #replace-preview {
  max-height: 60vh;
  overflow: auto;
}
#find-and-replace #replace-preview pre {
  padding: 5px 10px;
}
.terminal-app {
  background: #EEE;
}
.terminal-app #header {
  background: #fff;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.2);
}
.terminal-app .terminal {
  width: 100%;
  float: left;
  font-family: monospace;
  color: white;
  background: black;
  padding: 0.4em;
  border-radius: 2px;
  -webkit-box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
  box-shadow: 0px 0px 12px 1px rgba(87, 87, 87, 0.4);
}
.terminal-app .terminal,
.terminal-app .terminal dummy-screen {
  line-height: 1em;
  font-size: 14px;
}
.terminal-app .terminal .xterm-rows {
  padding: 10px;
}
.terminal-app .terminal-cursor {
  color: black;
  background: white;
}
.terminal-app #terminado-container {
  margin-top: 20px;
}
/*# sourceMappingURL=style.min.css.map */
    </style>
<style type="text/css">
    .highlight .hll { background-color: #ffffcc }
.highlight  { background: #f8f8f8; }
.highlight .c { color: #408080; font-style: italic } /* Comment */
.highlight .err { border: 1px solid #FF0000 } /* Error */
.highlight .k { color: #008000; font-weight: bold } /* Keyword */
.highlight .o { color: #666666 } /* Operator */
.highlight .ch { color: #408080; font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: #408080; font-style: italic } /* Comment.Multiline */
.highlight .cp { color: #BC7A00 } /* Comment.Preproc */
.highlight .cpf { color: #408080; font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: #408080; font-style: italic } /* Comment.Single */
.highlight .cs { color: #408080; font-style: italic } /* Comment.Special */
.highlight .gd { color: #A00000 } /* Generic.Deleted */
.highlight .ge { font-style: italic } /* Generic.Emph */
.highlight .gr { color: #FF0000 } /* Generic.Error */
.highlight .gh { color: #000080; font-weight: bold } /* Generic.Heading */
.highlight .gi { color: #00A000 } /* Generic.Inserted */
.highlight .go { color: #888888 } /* Generic.Output */
.highlight .gp { color: #000080; font-weight: bold } /* Generic.Prompt */
.highlight .gs { font-weight: bold } /* Generic.Strong */
.highlight .gu { color: #800080; font-weight: bold } /* Generic.Subheading */
.highlight .gt { color: #0044DD } /* Generic.Traceback */
.highlight .kc { color: #008000; font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: #008000; font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: #008000; font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: #008000 } /* Keyword.Pseudo */
.highlight .kr { color: #008000; font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: #B00040 } /* Keyword.Type */
.highlight .m { color: #666666 } /* Literal.Number */
.highlight .s { color: #BA2121 } /* Literal.String */
.highlight .na { color: #7D9029 } /* Name.Attribute */
.highlight .nb { color: #008000 } /* Name.Builtin */
.highlight .nc { color: #0000FF; font-weight: bold } /* Name.Class */
.highlight .no { color: #880000 } /* Name.Constant */
.highlight .nd { color: #AA22FF } /* Name.Decorator */
.highlight .ni { color: #999999; font-weight: bold } /* Name.Entity */
.highlight .ne { color: #D2413A; font-weight: bold } /* Name.Exception */
.highlight .nf { color: #0000FF } /* Name.Function */
.highlight .nl { color: #A0A000 } /* Name.Label */
.highlight .nn { color: #0000FF; font-weight: bold } /* Name.Namespace */
.highlight .nt { color: #008000; font-weight: bold } /* Name.Tag */
.highlight .nv { color: #19177C } /* Name.Variable */
.highlight .ow { color: #AA22FF; font-weight: bold } /* Operator.Word */
.highlight .w { color: #bbbbbb } /* Text.Whitespace */
.highlight .mb { color: #666666 } /* Literal.Number.Bin */
.highlight .mf { color: #666666 } /* Literal.Number.Float */
.highlight .mh { color: #666666 } /* Literal.Number.Hex */
.highlight .mi { color: #666666 } /* Literal.Number.Integer */
.highlight .mo { color: #666666 } /* Literal.Number.Oct */
.highlight .sa { color: #BA2121 } /* Literal.String.Affix */
.highlight .sb { color: #BA2121 } /* Literal.String.Backtick */
.highlight .sc { color: #BA2121 } /* Literal.String.Char */
.highlight .dl { color: #BA2121 } /* Literal.String.Delimiter */
.highlight .sd { color: #BA2121; font-style: italic } /* Literal.String.Doc */
.highlight .s2 { color: #BA2121 } /* Literal.String.Double */
.highlight .se { color: #BB6622; font-weight: bold } /* Literal.String.Escape */
.highlight .sh { color: #BA2121 } /* Literal.String.Heredoc */
.highlight .si { color: #BB6688; font-weight: bold } /* Literal.String.Interpol */
.highlight .sx { color: #008000 } /* Literal.String.Other */
.highlight .sr { color: #BB6688 } /* Literal.String.Regex */
.highlight .s1 { color: #BA2121 } /* Literal.String.Single */
.highlight .ss { color: #19177C } /* Literal.String.Symbol */
.highlight .bp { color: #008000 } /* Name.Builtin.Pseudo */
.highlight .fm { color: #0000FF } /* Name.Function.Magic */
.highlight .vc { color: #19177C } /* Name.Variable.Class */
.highlight .vg { color: #19177C } /* Name.Variable.Global */
.highlight .vi { color: #19177C } /* Name.Variable.Instance */
.highlight .vm { color: #19177C } /* Name.Variable.Magic */
.highlight .il { color: #666666 } /* Literal.Number.Integer.Long */
    </style>


<style type="text/css">
/* Overrides of notebook CSS for static HTML export */
body {
  overflow: visible;
  padding: 8px;
}

div#notebook {
  overflow: visible;
  border-top: none;
}@media print {
  div.cell {
    display: block;
    page-break-inside: avoid;
  } 
  div.output_wrapper { 
    display: block;
    page-break-inside: avoid; 
  }
  div.output { 
    display: block;
    page-break-inside: avoid; 
  }
}
</style>

<!-- Custom stylesheet, it must be in the same directory as the html file -->
<link rel="stylesheet" href="custom.css">

<!-- Loading mathjax macro -->
<!-- Load mathjax -->
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.5/latest.js?config=TeX-AMS_HTML"></script>
    <!-- MathJax configuration -->
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
        tex2jax: {
            inlineMath: [ ['$','$'], ["\\(","\\)"] ],
            displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
            processEscapes: true,
            processEnvironments: true
        },
        // Center justify equations in code and markdown cells. Elsewhere
        // we use CSS to left justify single line equations in code cells.
        displayAlign: 'center',
        "HTML-CSS": {
            styles: {'.MathJax_Display': {"margin": 0}},
            linebreaks: { automatic: true }
        }
    });
    </script>
    <!-- End of mathjax configuration --></head>
<body>
  <div tabindex="-1" id="notebook" class="border-box-sizing">
    <div class="container" id="notebook-container">

<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Import-The-Dataset">Import The Dataset<a class="anchor-link" href="#Import-The-Dataset">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[16]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">torch</span>
<span class="kn">import</span> <span class="nn">torchvision</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="kn">from</span> <span class="nn">time</span> <span class="kn">import</span> <span class="n">time</span>
<span class="kn">from</span> <span class="nn">torchvision</span> <span class="kn">import</span> <span class="n">datasets</span><span class="p">,</span> <span class="n">transforms</span>
<span class="kn">from</span> <span class="nn">torch</span> <span class="kn">import</span> <span class="n">nn</span><span class="p">,</span> <span class="n">optim</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Code-for-images-having-the-same-dimensions-and-properties.">Code for images having the same dimensions and properties.<a class="anchor-link" href="#Code-for-images-having-the-same-dimensions-and-properties.">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[17]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">transform</span> <span class="o">=</span> <span class="n">transforms</span><span class="o">.</span><span class="n">Compose</span><span class="p">([</span><span class="n">transforms</span><span class="o">.</span><span class="n">ToTensor</span><span class="p">(),</span>
                              <span class="n">transforms</span><span class="o">.</span><span class="n">Normalize</span><span class="p">((</span><span class="mf">0.5</span><span class="p">,),</span> <span class="p">(</span><span class="mf">0.5</span><span class="p">,)),</span>
                              <span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Download-the-data-sets-and-load-them-to-DataLoader">Download the data sets and load them to DataLoader<a class="anchor-link" href="#Download-the-data-sets-and-load-them-to-DataLoader">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[18]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">trainset</span> <span class="o">=</span> <span class="n">datasets</span><span class="o">.</span><span class="n">MNIST</span><span class="p">(</span><span class="s1">&#39;PATH_TO_STORE_TRAINSET&#39;</span><span class="p">,</span> <span class="n">download</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">train</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">transform</span><span class="o">=</span><span class="n">transform</span><span class="p">)</span>
<span class="n">valset</span> <span class="o">=</span> <span class="n">datasets</span><span class="o">.</span><span class="n">MNIST</span><span class="p">(</span><span class="s1">&#39;PATH_TO_STORE_TESTSET&#39;</span><span class="p">,</span> <span class="n">download</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">train</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">transform</span><span class="o">=</span><span class="n">transform</span><span class="p">)</span>
<span class="n">trainloader</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">utils</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">DataLoader</span><span class="p">(</span><span class="n">trainset</span><span class="p">,</span> <span class="n">batch_size</span><span class="o">=</span><span class="mi">64</span><span class="p">,</span> <span class="n">shuffle</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="n">valloader</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">utils</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">DataLoader</span><span class="p">(</span><span class="n">valset</span><span class="p">,</span> <span class="n">batch_size</span><span class="o">=</span><span class="mi">64</span><span class="p">,</span> <span class="n">shuffle</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Shape-the-images-and-the-labels">Shape the images and the labels<a class="anchor-link" href="#Shape-the-images-and-the-labels">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[19]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataiter</span> <span class="o">=</span> <span class="nb">iter</span><span class="p">(</span><span class="n">trainloader</span><span class="p">)</span>
<span class="n">images</span><span class="p">,</span> <span class="n">labels</span> <span class="o">=</span> <span class="n">dataiter</span><span class="o">.</span><span class="n">next</span><span class="p">()</span>

<span class="nb">print</span><span class="p">(</span><span class="n">images</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">labels</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>torch.Size([64, 1, 28, 28])
torch.Size([64])
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Display-one-image-from-the-training-set">Display one image from the training set<a class="anchor-link" href="#Display-one-image-from-the-training-set">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[20]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">images</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(),</span> <span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray_r&#39;</span><span class="p">);</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Show-how-the-dataset-looks-like.">Show how the dataset looks like.<a class="anchor-link" href="#Show-how-the-dataset-looks-like.">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[21]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">figure</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">()</span>
<span class="n">num_of_images</span> <span class="o">=</span> <span class="mi">60</span>
<span class="k">for</span> <span class="n">index</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="n">num_of_images</span> <span class="o">+</span> <span class="mi">1</span><span class="p">):</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="n">index</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">axis</span><span class="p">(</span><span class="s1">&#39;off&#39;</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">images</span><span class="p">[</span><span class="n">index</span><span class="p">]</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">squeeze</span><span class="p">(),</span> <span class="n">cmap</span><span class="o">=</span><span class="s1">&#39;gray_r&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Build-the-neural-network">Build the neural network<a class="anchor-link" href="#Build-the-neural-network">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[22]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">input_size</span> <span class="o">=</span> <span class="mi">784</span>
<span class="n">hidden_sizes</span> <span class="o">=</span> <span class="p">[</span><span class="mi">128</span><span class="p">,</span> <span class="mi">64</span><span class="p">]</span>
<span class="n">output_size</span> <span class="o">=</span> <span class="mi">10</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">nn</span><span class="o">.</span><span class="n">Sequential</span><span class="p">(</span><span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="n">input_size</span><span class="p">,</span> <span class="n">hidden_sizes</span><span class="p">[</span><span class="mi">0</span><span class="p">]),</span>
                      <span class="n">nn</span><span class="o">.</span><span class="n">ReLU</span><span class="p">(),</span>
                      <span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="n">hidden_sizes</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">hidden_sizes</span><span class="p">[</span><span class="mi">1</span><span class="p">]),</span>
                      <span class="n">nn</span><span class="o">.</span><span class="n">ReLU</span><span class="p">(),</span>
                      <span class="n">nn</span><span class="o">.</span><span class="n">Linear</span><span class="p">(</span><span class="n">hidden_sizes</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span> <span class="n">output_size</span><span class="p">),</span>
                      <span class="n">nn</span><span class="o">.</span><span class="n">LogSoftmax</span><span class="p">(</span><span class="n">dim</span><span class="o">=</span><span class="mi">1</span><span class="p">))</span>
<span class="nb">print</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Sequential(
  (0): Linear(in_features=784, out_features=128, bias=True)
  (1): ReLU()
  (2): Linear(in_features=128, out_features=64, bias=True)
  (3): ReLU()
  (4): Linear(in_features=64, out_features=10, bias=True)
  (5): LogSoftmax(dim=1)
)
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[23]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">criterion</span> <span class="o">=</span> <span class="n">nn</span><span class="o">.</span><span class="n">NLLLoss</span><span class="p">()</span>
<span class="n">images</span><span class="p">,</span> <span class="n">labels</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">trainloader</span><span class="p">))</span>
<span class="n">images</span> <span class="o">=</span> <span class="n">images</span><span class="o">.</span><span class="n">view</span><span class="p">(</span><span class="n">images</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>

<span class="n">logps</span> <span class="o">=</span> <span class="n">model</span><span class="p">(</span><span class="n">images</span><span class="p">)</span> <span class="c1">#log probabilities</span>
<span class="n">loss</span> <span class="o">=</span> <span class="n">criterion</span><span class="p">(</span><span class="n">logps</span><span class="p">,</span> <span class="n">labels</span><span class="p">)</span> <span class="c1">#calculate the NLL loss</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Adjusting-Weights">Adjusting Weights<a class="anchor-link" href="#Adjusting-Weights">&#182;</a></h1>
</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[24]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="s1">&#39;Before backward pass: </span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">model</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">weight</span><span class="o">.</span><span class="n">grad</span><span class="p">)</span>
<span class="n">loss</span><span class="o">.</span><span class="n">backward</span><span class="p">()</span>
<span class="nb">print</span><span class="p">(</span><span class="s1">&#39;After backward pass: </span><span class="se">\n</span><span class="s1">&#39;</span><span class="p">,</span> <span class="n">model</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">weight</span><span class="o">.</span><span class="n">grad</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Before backward pass: 
 None
After backward pass: 
 tensor([[ 1.5143e-03,  1.5143e-03,  1.5143e-03,  ...,  1.5143e-03,
          1.5143e-03,  1.5143e-03],
        [ 5.4715e-04,  5.4715e-04,  5.4715e-04,  ...,  5.4715e-04,
          5.4715e-04,  5.4715e-04],
        [-2.9231e-03, -2.9231e-03, -2.9231e-03,  ..., -2.9231e-03,
         -2.9231e-03, -2.9231e-03],
        ...,
        [ 6.3725e-06,  6.3725e-06,  6.3725e-06,  ...,  6.3725e-06,
          6.3725e-06,  6.3725e-06],
        [-2.4908e-03, -2.4908e-03, -2.4908e-03,  ..., -2.4908e-03,
         -2.4908e-03, -2.4908e-03],
        [-1.2771e-03, -1.2771e-03, -1.2771e-03,  ..., -1.2771e-03,
         -1.2771e-03, -1.2771e-03]])
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="neural-network-iterates-over-the-training-set-and-updates-the-weights.">neural network iterates over the training set and updates the weights.<a class="anchor-link" href="#neural-network-iterates-over-the-training-set-and-updates-the-weights.">&#182;</a></h1><p>Number of times we iterate over the training set, we will be seeing a gradual decrease in training loss.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[25]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">optimizer</span> <span class="o">=</span> <span class="n">optim</span><span class="o">.</span><span class="n">SGD</span><span class="p">(</span><span class="n">model</span><span class="o">.</span><span class="n">parameters</span><span class="p">(),</span> <span class="n">lr</span><span class="o">=</span><span class="mf">0.003</span><span class="p">,</span> <span class="n">momentum</span><span class="o">=</span><span class="mf">0.9</span><span class="p">)</span>
<span class="n">time0</span> <span class="o">=</span> <span class="n">time</span><span class="p">()</span>
<span class="n">epochs</span> <span class="o">=</span> <span class="mi">15</span>
<span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="n">epochs</span><span class="p">):</span>
    <span class="n">running_loss</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">images</span><span class="p">,</span> <span class="n">labels</span> <span class="ow">in</span> <span class="n">trainloader</span><span class="p">:</span>
        <span class="c1"># Flatten MNIST images into a 784 long vector</span>
        <span class="n">images</span> <span class="o">=</span> <span class="n">images</span><span class="o">.</span><span class="n">view</span><span class="p">(</span><span class="n">images</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="o">-</span><span class="mi">1</span><span class="p">)</span>
    
        <span class="c1"># Training pass</span>
        <span class="n">optimizer</span><span class="o">.</span><span class="n">zero_grad</span><span class="p">()</span>
        
        <span class="n">output</span> <span class="o">=</span> <span class="n">model</span><span class="p">(</span><span class="n">images</span><span class="p">)</span>
        <span class="n">loss</span> <span class="o">=</span> <span class="n">criterion</span><span class="p">(</span><span class="n">output</span><span class="p">,</span> <span class="n">labels</span><span class="p">)</span>
        
        <span class="c1">#This is where the model learns by backpropagating</span>
        <span class="n">loss</span><span class="o">.</span><span class="n">backward</span><span class="p">()</span>
        
        <span class="c1">#And optimizes its weights here</span>
        <span class="n">optimizer</span><span class="o">.</span><span class="n">step</span><span class="p">()</span>
        
        <span class="n">running_loss</span> <span class="o">+=</span> <span class="n">loss</span><span class="o">.</span><span class="n">item</span><span class="p">()</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Epoch </span><span class="si">{}</span><span class="s2"> - Training loss: </span><span class="si">{}</span><span class="s2">&quot;</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="n">running_loss</span><span class="o">/</span><span class="nb">len</span><span class="p">(</span><span class="n">trainloader</span><span class="p">)))</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">Training Time (in minutes) =&quot;</span><span class="p">,(</span><span class="n">time</span><span class="p">()</span><span class="o">-</span><span class="n">time0</span><span class="p">)</span><span class="o">/</span><span class="mi">60</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Epoch 0 - Training loss: 0.6287401923095621
Epoch 1 - Training loss: 0.280011943869118
Epoch 2 - Training loss: 0.21626190688691413
Epoch 3 - Training loss: 0.17675491470073076
Epoch 4 - Training loss: 0.1480448223185787
Epoch 5 - Training loss: 0.1277336039886212
Epoch 6 - Training loss: 0.11238295687382409
Epoch 7 - Training loss: 0.09869339859990804
Epoch 8 - Training loss: 0.08817634185247902
Epoch 9 - Training loss: 0.08044923931908315
Epoch 10 - Training loss: 0.07283765910022548
Epoch 11 - Training loss: 0.06676739336066902
Epoch 12 - Training loss: 0.06144485469691074
Epoch 13 - Training loss: 0.05647031735849263
Epoch 14 - Training loss: 0.05220964118870083

Training Time (in minutes) = 5.246107661724091
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Testing-&amp;-Evaluation">Testing &amp; Evaluation<a class="anchor-link" href="#Testing-&amp;-Evaluation">&#182;</a></h1><p>to see how the model works.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[26]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="k">def</span> <span class="nf">view_classify</span><span class="p">(</span><span class="n">img</span><span class="p">,</span> <span class="n">ps</span><span class="p">):</span>
    <span class="sd">&#39;&#39;&#39; Function for viewing an image and it&#39;s predicted classes.</span>
<span class="sd">    &#39;&#39;&#39;</span>
    <span class="n">ps</span> <span class="o">=</span> <span class="n">ps</span><span class="o">.</span><span class="n">cpu</span><span class="p">()</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">squeeze</span><span class="p">()</span>

    <span class="n">fig</span><span class="p">,</span> <span class="p">(</span><span class="n">ax1</span><span class="p">,</span> <span class="n">ax2</span><span class="p">)</span> <span class="o">=</span> <span class="n">plt</span><span class="o">.</span><span class="n">subplots</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">6</span><span class="p">,</span><span class="mi">9</span><span class="p">),</span> <span class="n">ncols</span><span class="o">=</span><span class="mi">2</span><span class="p">)</span>
    <span class="n">ax1</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">img</span><span class="o">.</span><span class="n">resize_</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">28</span><span class="p">,</span> <span class="mi">28</span><span class="p">)</span><span class="o">.</span><span class="n">numpy</span><span class="p">()</span><span class="o">.</span><span class="n">squeeze</span><span class="p">())</span>
    <span class="n">ax1</span><span class="o">.</span><span class="n">axis</span><span class="p">(</span><span class="s1">&#39;off&#39;</span><span class="p">)</span>
    <span class="n">ax2</span><span class="o">.</span><span class="n">barh</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">10</span><span class="p">),</span> <span class="n">ps</span><span class="p">)</span>
    <span class="n">ax2</span><span class="o">.</span><span class="n">set_aspect</span><span class="p">(</span><span class="mf">0.1</span><span class="p">)</span>
    <span class="n">ax2</span><span class="o">.</span><span class="n">set_yticks</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>
    <span class="n">ax2</span><span class="o">.</span><span class="n">set_yticklabels</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">arange</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>
    <span class="n">ax2</span><span class="o">.</span><span class="n">set_title</span><span class="p">(</span><span class="s1">&#39;Class Probability&#39;</span><span class="p">)</span>
    <span class="n">ax2</span><span class="o">.</span><span class="n">set_xlim</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mf">1.1</span><span class="p">)</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">tight_layout</span><span class="p">()</span>
    
    <span class="n">images</span><span class="p">,</span> <span class="n">labels</span> <span class="o">=</span> <span class="nb">next</span><span class="p">(</span><span class="nb">iter</span><span class="p">(</span><span class="n">valloader</span><span class="p">))</span>

<span class="n">img</span> <span class="o">=</span> <span class="n">images</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">view</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">784</span><span class="p">)</span>
<span class="k">with</span> <span class="n">torch</span><span class="o">.</span><span class="n">no_grad</span><span class="p">():</span>
    <span class="n">logps</span> <span class="o">=</span> <span class="n">model</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>

<span class="n">ps</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="n">logps</span><span class="p">)</span>
<span class="n">probab</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">ps</span><span class="o">.</span><span class="n">numpy</span><span class="p">()[</span><span class="mi">0</span><span class="p">])</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Predicted Digit =&quot;</span><span class="p">,</span> <span class="n">probab</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">probab</span><span class="p">)))</span>
<span class="n">view_classify</span><span class="p">(</span><span class="n">img</span><span class="o">.</span><span class="n">view</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">28</span><span class="p">,</span> <span class="mi">28</span><span class="p">),</span> <span class="n">ps</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Predicted Digit = 0
</pre>
</div>
</div>

<div class="output_area">

    <div class="prompt"></div>




<div class="output_png output_subarea ">
<img src="data:image/png;base64,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
"
>
</div>

</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="calculate-the-accuracy.">calculate the accuracy.<a class="anchor-link" href="#calculate-the-accuracy.">&#182;</a></h1><p>Result</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[27]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">correct_count</span><span class="p">,</span> <span class="n">all_count</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="mi">0</span>
<span class="k">for</span> <span class="n">images</span><span class="p">,</span><span class="n">labels</span> <span class="ow">in</span> <span class="n">valloader</span><span class="p">:</span>
  <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="nb">len</span><span class="p">(</span><span class="n">labels</span><span class="p">)):</span>
    <span class="n">img</span> <span class="o">=</span> <span class="n">images</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="o">.</span><span class="n">view</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">784</span><span class="p">)</span>
    <span class="k">with</span> <span class="n">torch</span><span class="o">.</span><span class="n">no_grad</span><span class="p">():</span>
        <span class="n">logps</span> <span class="o">=</span> <span class="n">model</span><span class="p">(</span><span class="n">img</span><span class="p">)</span>

    
    <span class="n">ps</span> <span class="o">=</span> <span class="n">torch</span><span class="o">.</span><span class="n">exp</span><span class="p">(</span><span class="n">logps</span><span class="p">)</span>
    <span class="n">probab</span> <span class="o">=</span> <span class="nb">list</span><span class="p">(</span><span class="n">ps</span><span class="o">.</span><span class="n">numpy</span><span class="p">()[</span><span class="mi">0</span><span class="p">])</span>
    <span class="n">pred_label</span> <span class="o">=</span> <span class="n">probab</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="nb">max</span><span class="p">(</span><span class="n">probab</span><span class="p">))</span>
    <span class="n">true_label</span> <span class="o">=</span> <span class="n">labels</span><span class="o">.</span><span class="n">numpy</span><span class="p">()[</span><span class="n">i</span><span class="p">]</span>
    <span class="k">if</span><span class="p">(</span><span class="n">true_label</span> <span class="o">==</span> <span class="n">pred_label</span><span class="p">):</span>
      <span class="n">correct_count</span> <span class="o">+=</span> <span class="mi">1</span>
    <span class="n">all_count</span> <span class="o">+=</span> <span class="mi">1</span>

<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;Number Of Images Tested =&quot;</span><span class="p">,</span> <span class="n">all_count</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="s2">&quot;</span><span class="se">\n</span><span class="s2">Model Accuracy =&quot;</span><span class="p">,</span> <span class="p">(</span><span class="n">correct_count</span><span class="o">/</span><span class="n">all_count</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_stream output_stdout output_text">
<pre>Number Of Images Tested = 10000

Model Accuracy = 0.9756
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing text_cell rendered"><div class="prompt input_prompt">
</div><div class="inner_cell">
<div class="text_cell_render border-box-sizing rendered_html">
<h1 id="Saving-The-Model">Saving The Model<a class="anchor-link" href="#Saving-The-Model">&#182;</a></h1><p>we can load it and use it directly without further training.</p>

</div>
</div>
</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[28]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">torch</span><span class="o">.</span><span class="n">save</span><span class="p">(</span><span class="n">model</span><span class="p">,</span> <span class="s1">&#39;./my_mnist_model.pt&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">from</span> <span class="nn">sklearn</span> <span class="kn">import</span> <span class="n">preprocessing</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span> 
<span class="n">plt</span><span class="o">.</span><span class="n">rc</span><span class="p">(</span><span class="s2">&quot;font&quot;</span><span class="p">,</span> <span class="n">size</span><span class="o">=</span><span class="mi">14</span><span class="p">)</span>
<span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LogisticRegression</span>
<span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>
<span class="kn">import</span> <span class="nn">seaborn</span> <span class="k">as</span> <span class="nn">sns</span>
<span class="n">sns</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">style</span><span class="o">=</span><span class="s2">&quot;white&quot;</span><span class="p">)</span>
<span class="n">sns</span><span class="o">.</span><span class="n">set</span><span class="p">(</span><span class="n">style</span><span class="o">=</span><span class="s2">&quot;whitegrid&quot;</span><span class="p">,</span> <span class="n">color_codes</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>


<span class="n">dataset</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_csv</span><span class="p">(</span><span class="s1">&#39;E://mnist_test/mnist_test.csv&#39;</span><span class="p">)</span>
<span class="n">dataset</span><span class="o">.</span><span class="n">head</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">dataset</span><span class="p">[</span><span class="s1">&#39;label&#39;</span><span class="p">]</span><span class="o">.</span><span class="n">unique</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.datasets</span> <span class="kn">import</span> <span class="n">load_digits</span>
<span class="n">digits</span> <span class="o">=</span> <span class="n">load_digits</span><span class="p">()</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span> 
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span><span class="mi">4</span><span class="p">))</span>
<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">label</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">digits</span><span class="o">.</span><span class="n">data</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">5</span><span class="p">],</span> <span class="n">digits</span><span class="o">.</span><span class="n">target</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">5</span><span class="p">])):</span>
 <span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
 <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="p">(</span><span class="mi">8</span><span class="p">,</span><span class="mi">8</span><span class="p">)),</span> <span class="n">cmap</span><span class="o">=</span><span class="n">plt</span><span class="o">.</span><span class="n">cm</span><span class="o">.</span><span class="n">gray</span><span class="p">)</span>
 <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Training: </span><span class="si">%i</span><span class="se">\n</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="n">label</span><span class="p">,</span> <span class="n">fontsize</span> <span class="o">=</span> <span class="mi">20</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>
<span class="n">x_train</span><span class="p">,</span> <span class="n">x_test</span><span class="p">,</span> <span class="n">y_train</span><span class="p">,</span> <span class="n">y_test</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span><span class="n">digits</span><span class="o">.</span><span class="n">data</span><span class="p">,</span> <span class="n">digits</span><span class="o">.</span><span class="n">target</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mf">0.25</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LogisticRegression</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">logisticRegr</span> <span class="o">=</span> <span class="n">LogisticRegression</span><span class="p">()</span>
<span class="n">logisticRegr</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">x_train</span><span class="p">,</span> <span class="n">y_train</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">logisticRegr</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">x_test</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="o">-</span><span class="mi">1</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">logisticRegr</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">x_test</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">10</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">predictions</span> <span class="o">=</span> <span class="n">logisticRegr</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">x_test</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">score</span> <span class="o">=</span> <span class="n">logisticRegr</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">x_test</span><span class="p">,</span> <span class="n">y_test</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">score</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.datasets</span> <span class="kn">import</span> <span class="n">fetch_openml</span>
<span class="n">mnist</span> <span class="o">=</span> <span class="n">fetch_openml</span><span class="p">(</span><span class="s1">&#39;mnist_784&#39;</span><span class="p">)</span>
<span class="n">mnist</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="nb">print</span><span class="p">(</span><span class="n">mnist</span><span class="o">.</span><span class="n">data</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
<span class="c1"># These are the labels</span>
<span class="nb">print</span><span class="p">(</span><span class="n">mnist</span><span class="o">.</span><span class="n">target</span><span class="o">.</span><span class="n">shape</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.model_selection</span> <span class="kn">import</span> <span class="n">train_test_split</span>
<span class="n">train_img</span><span class="p">,</span> <span class="n">test_img</span><span class="p">,</span> <span class="n">train_lbl</span><span class="p">,</span> <span class="n">test_lbl</span> <span class="o">=</span> <span class="n">train_test_split</span><span class="p">(</span>
 <span class="n">mnist</span><span class="o">.</span><span class="n">data</span><span class="p">,</span> <span class="n">mnist</span><span class="o">.</span><span class="n">target</span><span class="p">,</span> <span class="n">test_size</span><span class="o">=</span><span class="mi">1</span><span class="o">/</span><span class="mf">7.0</span><span class="p">,</span> <span class="n">random_state</span><span class="o">=</span><span class="mi">0</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span>
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span><span class="mi">4</span><span class="p">))</span>
<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="n">label</span><span class="p">)</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="nb">zip</span><span class="p">(</span><span class="n">train_img</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">5</span><span class="p">],</span> <span class="n">train_lbl</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">5</span><span class="p">])):</span>
 <span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="n">index</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
 <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="n">image</span><span class="p">,</span> <span class="p">(</span><span class="mi">28</span><span class="p">,</span><span class="mi">28</span><span class="p">)),</span> <span class="n">cmap</span><span class="o">=</span><span class="n">plt</span><span class="o">.</span><span class="n">cm</span><span class="o">.</span><span class="n">gray</span><span class="p">)</span>
 <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="s1">&#39;Training: </span><span class="si">%i</span><span class="se">\n</span><span class="s1">&#39;</span> <span class="o">%</span> <span class="n">label</span><span class="p">,</span> <span class="n">fontsize</span> <span class="o">=</span> <span class="mi">20</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">sklearn.linear_model</span> <span class="kn">import</span> <span class="n">LogisticRegression</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># default solver is incredibly slow thats why we change it</span>
<span class="n">logisticRegr</span> <span class="o">=</span> <span class="n">LogisticRegression</span><span class="p">(</span><span class="n">solver</span> <span class="o">=</span> <span class="s1">&#39;lbfgs&#39;</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">logisticRegr</span><span class="o">.</span><span class="n">fit</span><span class="p">(</span><span class="n">train_img</span><span class="p">,</span> <span class="n">train_lbl</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="c1"># Returns a NumPy Array</span>
<span class="c1"># Predict for One Observation (image)</span>
<span class="n">logisticRegr</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">test_img</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span><span class="o">-</span><span class="mi">1</span><span class="p">))</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">logisticRegr</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">test_img</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">10</span><span class="p">])</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">predictions</span> <span class="o">=</span> <span class="n">logisticRegr</span><span class="o">.</span><span class="n">predict</span><span class="p">(</span><span class="n">test_img</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[31]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">score</span> <span class="o">=</span> <span class="n">logisticRegr</span><span class="o">.</span><span class="n">score</span><span class="p">(</span><span class="n">test_img</span><span class="p">,</span> <span class="n">test_lbl</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">accuracy</span><span class="p">:)</span>
</pre></div>

    </div>
</div>
</div>

<div class="output_wrapper">
<div class="output">


<div class="output_area">

    <div class="prompt"></div>


<div class="output_subarea output_text output_error">
<pre>
<span class="ansi-cyan-intense-fg ansi-bold">  File </span><span class="ansi-green-intense-fg ansi-bold">&#34;&lt;ipython-input-31-04364fc14ee4&gt;&#34;</span><span class="ansi-cyan-intense-fg ansi-bold">, line </span><span class="ansi-green-intense-fg ansi-bold">2</span>
<span class="ansi-yellow-intense-fg ansi-bold">    print(accuracy:)</span>
<span class="ansi-white-intense-fg ansi-bold">                  ^</span>
<span class="ansi-red-intense-fg ansi-bold">SyntaxError</span><span class="ansi-red-intense-fg ansi-bold">:</span> invalid syntax
</pre>
</div>
</div>

</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">numpy</span> <span class="k">as</span> <span class="nn">np</span> 
<span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>
<span class="n">index</span> <span class="o">=</span> <span class="mi">0</span>
<span class="n">misclassifiedIndexes</span> <span class="o">=</span> <span class="p">[]</span>
<span class="k">for</span> <span class="n">label</span><span class="p">,</span> <span class="n">predict</span> <span class="ow">in</span> <span class="nb">zip</span><span class="p">(</span><span class="n">test_lbl</span><span class="p">,</span> <span class="n">predictions</span><span class="p">):</span>
 <span class="k">if</span> <span class="n">label</span> <span class="o">!=</span> <span class="n">predict</span><span class="p">:</span> 
  <span class="n">misclassifiedIndexes</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">index</span><span class="p">)</span>
  <span class="n">index</span> <span class="o">+=</span><span class="mi">1</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span><span class="n">plt</span><span class="o">.</span><span class="n">figure</span><span class="p">(</span><span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">20</span><span class="p">,</span><span class="mi">4</span><span class="p">))</span>
<span class="k">for</span> <span class="n">plotIndex</span><span class="p">,</span> <span class="n">badIndex</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">misclassifiedIndexes</span><span class="p">[</span><span class="mi">0</span><span class="p">:</span><span class="mi">5</span><span class="p">]):</span>
 <span class="n">plt</span><span class="o">.</span><span class="n">subplot</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">5</span><span class="p">,</span> <span class="n">plotIndex</span> <span class="o">+</span> <span class="mi">1</span><span class="p">)</span>
 <span class="n">plt</span><span class="o">.</span><span class="n">imshow</span><span class="p">(</span><span class="n">np</span><span class="o">.</span><span class="n">reshape</span><span class="p">(</span><span class="n">test_img</span><span class="p">[</span><span class="n">badIndex</span><span class="p">],</span> <span class="p">(</span><span class="mi">28</span><span class="p">,</span><span class="mi">28</span><span class="p">)),</span> <span class="n">cmap</span><span class="o">=</span><span class="n">plt</span><span class="o">.</span><span class="n">cm</span><span class="o">.</span><span class="n">gray</span><span class="p">)</span>
 <span class="n">plt</span><span class="o">.</span><span class="n">title</span><span class="p">(</span><span class="err">‘</span><span class="n">Predicted</span><span class="p">:</span> <span class="p">{},</span> <span class="n">Actual</span><span class="p">:</span> <span class="p">{}</span><span class="err">’</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="n">predictions</span><span class="p">[</span><span class="n">badIndex</span><span class="p">],</span> <span class="n">test_lbl</span><span class="p">[</span><span class="n">badIndex</span><span class="p">]),</span> <span class="n">fontsize</span> <span class="o">=</span> <span class="mi">15</span><span class="p">)</span>
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
<div class="cell border-box-sizing code_cell rendered">
<div class="input">
<div class="prompt input_prompt">In&nbsp;[&nbsp;]:</div>
<div class="inner_cell">
    <div class="input_area">
<div class=" highlight hl-ipython3"><pre><span></span> 
</pre></div>

    </div>
</div>
</div>

</div>
    </div>
  </div>
</body>

 


</html>
