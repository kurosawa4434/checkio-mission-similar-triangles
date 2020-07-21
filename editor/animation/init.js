//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $) {
        function similarTriangesAnimation(tgt_node, data) {

            if (! data || ! data.ext) {
                return
            }

            const input = data.in
            const explanation = data.ext.explanation
            const answer = data.ext.answer

            /*----------------------------------------------*
             *
             * attr
             *
             *----------------------------------------------*/
            const attr = {
                triangle: {
                    similar: {
                        'stroke-width': '2px',
                        'stroke': '#F0801A',
                        'opacity': '0.7',
                        'fill': '#FABA00',
                    },
                    different: {
                        'stroke-width': '2px',
                        'stroke': '#294270',
                        'opacity': '0.7',
                        'fill': '#82D1F5',
                    },
                },
                grid: {
                    'stroke-width': '1px',
                    'stroke': '#82D1F5',
                },
                axis: {
                    'stroke-width': '1px',
                    'stroke': '#294270',
                    'arrow-end': 'block-wide-long',
                },
            };

            /*----------------------------------------------*
             *
             * values
             *
             *----------------------------------------------*/
            const grid_size_px = 300
            let min_height = -1
            let min_width = -1
            let max_height = 4
            let max_width = 0

            const fm = input.flatMap(i=>i)
            fm.forEach(([x, y])=>{
                min_height = Math.min(min_height, y)
                max_height = Math.max(max_height, y)
                min_width = Math.min(min_width, x)
                max_width = Math.max(max_width, x)
            })

            max_height += 1
            max_width += 1
            min_height -= 1
            min_width -= 1

            const width = max_width - min_width
            const height = max_height - min_height
            const max_units = Math.max(width, height)
            const unit = grid_size_px / max_units

            if (width > height) {
                max_height = width + min_height
            } else {
                max_width = height + min_width
            }

            /*----------------------------------------------*
             *
             * paper
             *
             *----------------------------------------------*/
            const paper = Raphael(tgt_node, grid_size_px, grid_size_px, 0, 0)

            /*----------------------------------------------*
             *
             * draw grid
             *
             *----------------------------------------------*/
            // horizontal
            for (let i = 0; i <= max_units; i += 1) {
                paper.path(['M', 0, i*unit, 'h', grid_size_px]).attr(attr.grid)
            }

            // vertical
            for (let i = 0; i <= max_units; i += 1) {
                paper.path(['M', i*unit, 0, 'v', grid_size_px]).attr(attr.grid)
            }

            /*----------------------------------------------*
             *
             * draw axis
             *
             *----------------------------------------------*/
            // horizontal
            paper.path(['M', 0, (max_height)*unit, 'h', grid_size_px-4]).attr(attr.axis)

            // vertical
            paper.path(['M', (min_width*-1)*unit, (max_units)*unit, 'v', -(grid_size_px-4)]).attr(attr.axis)

            /*----------------------------------------------*
             *
             * draw triangles
             *
             *----------------------------------------------*/
            let path = []
            for (let j = 0; j < 2; j += 1) {
                path = []
                for (let i = 0; i < 3; i += 1) {
                    const [x, y] = input[j][i]
                    path = path.concat([(i == 0 ? 'M': 'L'),
                                        (x-min_width)*unit,
                                        (max_height-y)*unit])
                }
                path.push('Z')
                paper.path(path).attr(
                    answer ? attr.triangle.similar : attr.triangle.different)
            }

            /*----------------------------------------------*
             *
             * origin O
             *
             *----------------------------------------------*/
            const x = -min_width*unit
            const y = max_height*unit
            paper.text(x-unit/4, y+unit/3, 0).attr({'font-size': 7/max_units*20})
        }

        var $tryit;

        var io = new extIO({
            multipleArguments: true,
            functions: {
                python: 'similar_triangles',
                js: 'similarTriangles'
            },
            animation: function($expl, data){
                similarTriangesAnimation(
                    $expl[0],
                    data,
                );
            }
        });
        io.start();
    }
);
