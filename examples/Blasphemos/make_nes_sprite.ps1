Add-Type -AssemblyName System.Drawing

$srcPath = "C:\Users\franc\.gemini\antigravity\brain\03fec54e-79e3-4151-a162-b7c2f2662ee1\penitent_climb_no_ladder_1776476972527.png"
$outPath = "c:\Workspace\NESFab\nesfab\examples\Blasphemos\assets\ladder_climb_NES.png"
$previewPath = "c:\Workspace\NESFab\nesfab\examples\Blasphemos\assets\ladder_climb_preview.png"

$src = [System.Drawing.Bitmap]::FromFile($srcPath)
$dest = New-Object System.Drawing.Bitmap 32, 32

$black = [System.Drawing.Color]::FromArgb(0, 0, 0)
$gray = [System.Drawing.Color]::FromArgb(85, 85, 85) # or match your sprite sheet gray
$white = [System.Drawing.Color]::FromArgb(255, 255, 255)

# Extract palette from the original sprite.png reference
# It uses strict black, white, and a specific gray.
for ($y = 0; $y -lt 32; $y++) {
    for ($x = 0; $x -lt 32; $x++) {
        # Sample the exact middle of each 32x32 block (1024 / 32 = 32)
        $px = $x * 32 + 16
        $py = $y * 32 + 16
        if ($px -ge $src.Width) { $px = $src.Width - 1 }
        if ($py -ge $src.Height) { $py = $src.Height - 1 }
        $color = $src.GetPixel($px, $py)

        # Calculate luminance/distance to snap to our strict 3 colors
        $brightness = ($color.R * 0.3 + $color.G * 0.59 + $color.B * 0.11)
        
        if ($brightness -lt 40) {
            $snap = $black
        } elseif ($brightness -gt 150) {
            $snap = $white
        } else {
            $snap = $gray
        }

        $dest.SetPixel($x, $y, $snap)
    }
}

$dest.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)

# Make a 128x128 preview purely for easy viewing in the chat using nearest neighbor
$preview = New-Object System.Drawing.Bitmap 128, 128
$g = [System.Drawing.Graphics]::FromImage($preview)
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::NearestNeighbor
$g.PixelOffsetMode = [System.Drawing.Drawing2D.PixelOffsetMode]::Half
$g.DrawImage($dest, 0, 0, 128, 128)
$g.Dispose()

$preview.Save($previewPath, [System.Drawing.Imaging.ImageFormat]::Png)

$src.Dispose()
$dest.Dispose()
$preview.Dispose()

Write-Host "True NES 32x32 Sprite created successfully."
