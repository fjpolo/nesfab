
Add-Type -AssemblyName System.Drawing

$bg1Path = "c:\Workspace\NES\nesfab\examples\LuciYFer\assets\bg1.png"
$refPath = "c:\Workspace\NES\nesfab\examples\LuciYFer\assets\reference_jail.png"

# Function to create Bone Bars Bitmap
function New-BoneBars {
    $bmp = New-Object System.Drawing.Bitmap 16, 16
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.Clear([System.Drawing.Color]::Black)
    
    # Draw Left Bone
    $grey = [System.Drawing.Color]::FromArgb(188,188,188)
    $white = [System.Drawing.Color]::FromArgb(252,252,252)
    
    # Left Column (x=4,5,6)
    for ($y=0; $y -lt 16; $y++) {
        $bmp.SetPixel(4, $y, $grey)
        $bmp.SetPixel(5, $y, $white)
        $bmp.SetPixel(6, $y, $grey)
        
        # Right Column (x=10,11,12)
        $bmp.SetPixel(10, $y, $grey)
        $bmp.SetPixel(11, $y, $white)
        $bmp.SetPixel(12, $y, $grey)
        
        # Knuckles
        if (($y % 6) -eq 0 -or ($y % 6) -eq 1) {
            $bmp.SetPixel(3, $y, $white)
            $bmp.SetPixel(7, $y, $white)
            $bmp.SetPixel(9, $y, $white)
            $bmp.SetPixel(13, $y, $white)
        }
    }
    $g.Dispose()
    return $bmp
}

# Load Images
Write-Host "Loading bg1..."
$bg1 = [System.Drawing.Image]::FromFile($bg1Path)
$bg1Bmp = New-Object System.Drawing.Bitmap $bg1
$bg1.Dispose()

# Load Ref
$hasRef = $false
if (Test-Path $refPath) {
    Write-Host "Loading reference jail..."
    $refBase = [System.Drawing.Image]::FromFile($refPath)
    $ref = New-Object System.Drawing.Bitmap 16, 16
    $gRef = [System.Drawing.Graphics]::FromImage($ref)
    $gRef.DrawImage($refBase, 0, 0, 16, 16)
    $gRef.Dispose()
    $refBase.Dispose()
    $hasRef = $true
} else {
    Write-Host "Reference jail not found."
}

# Create Bone Tile
$boneTile = New-BoneBars

# Scan and Replace
$replacements = 0
if ($hasRef) {
    for ($ty = 0; $ty -lt 128; $ty+=16) {
        for ($tx = 0; $tx -lt 128; $tx+=16) {
            
            # Compare Tile at tx,ty with Ref
            $match = $true
            # Check a few points (corners, center)
            $points = @(0, 7, 15)
            $diffCheck = 0
            
            # Simple MSE check on sampled points
            foreach ($py in $points) {
                foreach ($px in $points) {
                    $c1 = $bg1Bmp.GetPixel($tx+$px, $ty+$py)
                    $c2 = $ref.GetPixel($px, $py)
                    
                    $d = [Math]::Abs($c1.R - $c2.R) + [Math]::Abs($c1.G - $c2.G) + [Math]::Abs($c1.B - $c2.B)
                    if ($d -gt 100) { # Tolerance
                        $diffCheck++
                    }
                }
            }
            
            if ($diffCheck -lt 3) { # Allow some mismatches
                Write-Host "Match found at $tx, $ty. Replacing..."
                
                # Draw Bone Tile
                for ($y=0; $y -lt 16; $y++) {
                    for ($x=0; $x -lt 16; $x++) {
                        $bg1Bmp.SetPixel($tx+$x, $ty+$y, $boneTile.GetPixel($x, $y))
                    }
                }
                $replacements++
            }
        }
    }
}

if ($replacements -gt 0) {
    Write-Host "Saving..."
    $bg1Bmp.Save($bg1Path, [System.Drawing.Imaging.ImageFormat]::Png)
    Write-Host "Updated bg1 with Bone Bars ($replacements tiles)."
} else {
    Write-Host "No tiles matched."
}

$bg1Bmp.Dispose()
if ($hasRef) { $ref.Dispose() }
$boneTile.Dispose()
