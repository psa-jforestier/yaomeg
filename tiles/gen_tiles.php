<?php
/**
 ** split the tile all.png
 ** in different png file
 **/

$all = 'all.png';

$im_all = imagecreatefrompng($all) or die("Unable to call imagecreatefrompng");


for($y = 0; $y < 5; $y++)
{
  for ($x=0; $x < 4; $x++)
  {
    $im = imagecreate(3,3);
    echo "Copy sprite from ";
    echo ($x*4)+1, ", ",($y*13)+2;
    echo "\n";
    imagecopy($im, $im_all,
        0, 0, // dst_x, dst_y
        ($x*4)+1, ($y*13)+2, // src_x, src_y
        3, 3  // src_w, src_h
    );
    imagetruecolortopalette($im, false, 8);
    if(imagecolorstotal($im) != 0)
      imagepng($im, "tile${x}_${y}.png");

  }
  
}
$im = imagecreate(3,3);
imagecopy($im, $im_all,
  0, 0, // dst_x, dst_y
  1, 2, // src_x, src_y
  3, 3  // src_w, src_h
  );

//imagetruecolortopalette($im, false, 8);
imagepng($im, "tile0.png");