import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk38 :
    P2RoundedFactorCheckpointData.panel19FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd14_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd14 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨14, by decide⟩ := by
  exact panel19FlatComponentChunk38

end RHP2Bridge
