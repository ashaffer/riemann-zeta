import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel19FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel19FlatComponentChunk33

end RHP2Bridge
