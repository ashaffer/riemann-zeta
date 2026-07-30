import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk25 :
    P2RoundedFactorCheckpointData.panel19FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd1_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd1 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨1, by decide⟩ := by
  exact panel19FlatComponentChunk25

end RHP2Bridge
