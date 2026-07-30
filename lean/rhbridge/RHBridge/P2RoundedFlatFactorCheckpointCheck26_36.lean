import RHBridge.P2RoundedFlatFactorCheckpointData26

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel26FlatComponentChunk36 :
    P2RoundedFactorCheckpointData.panel26FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel26FlatOdd12_eq :
    P2RoundedFactorCheckpointData.panel26FlatOdd12 =
      (P2RoundedFactorCheckpointData.panel26TruncatedOddComponents).get ⟨12, by decide⟩ := by
  exact panel26FlatComponentChunk36

end RHP2Bridge
