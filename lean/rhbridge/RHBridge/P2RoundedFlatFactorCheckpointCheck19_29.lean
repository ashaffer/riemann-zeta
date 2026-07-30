import RHBridge.P2RoundedFlatFactorCheckpointData19

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel19FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel19FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel19FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel19FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel19TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel19FlatComponentChunk29

end RHP2Bridge
