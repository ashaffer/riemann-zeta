import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk34 :
    P2RoundedFactorCheckpointData.panel18FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨10, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd10_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd10 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨10, by decide⟩ := by
  exact panel18FlatComponentChunk34

end RHP2Bridge
