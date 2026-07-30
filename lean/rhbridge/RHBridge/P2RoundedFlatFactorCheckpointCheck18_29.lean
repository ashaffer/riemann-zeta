import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk29 :
    P2RoundedFactorCheckpointData.panel18FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨5, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd5_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd5 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨5, by decide⟩ := by
  exact panel18FlatComponentChunk29

end RHP2Bridge
