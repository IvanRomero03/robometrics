
cwd=$(realpath "$0")
src_dir=$(dirname "$cwd")/..

echo "src_dir: $src_dir"
echo "cwd: $cwd"


if ![ -d $src_dir/robometrics ]; then
    echo "robometrics dir not found"
    exit 1
fi

move_dist=false
if [ -d $src_dir/dist ]; then
    if [ -d $src_dir/dist.bak ]; then
        rm -rf $src_dir/dist.bak
    fi
    mkdir $src_dir/dist.bak
    mv $src_dir/dist $src_dir/dist.bak
    move_dist=true
fi 

python3 intake-and-serve-setup.py sdist bdist_wheel 

twine upload $src_dir/dist/*

if $move_dist; then
    mv $src_dir/dist.bak $src_dir/dist
fi
