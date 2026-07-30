import RHBridge.P2RoundedFlatFactorCheckpointData18

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel18FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel18FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel18FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel18FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel18TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel18FlatComponentChunk24

end RHP2Bridge
