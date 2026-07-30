import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk30 :
    P2RoundedFactorCheckpointData.panel26FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd6_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd6 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨6, by decide⟩ := by
  exact panel26FlatComponentChunk30

end RHP2Bridge
