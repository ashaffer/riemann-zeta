import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk24 :
    P2RoundedFactorCheckpointData.panel26FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd0_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd0 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨0, by decide⟩ := by
  exact panel26FlatComponentChunk24

end RHP2Bridge
