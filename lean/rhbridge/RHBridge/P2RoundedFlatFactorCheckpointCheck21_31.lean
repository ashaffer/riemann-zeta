import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk31 :
    P2RoundedFactorCheckpointData.panel21FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨7, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd7_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd7 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨7, by decide⟩ := by
  exact panel21FlatComponentChunk31

end RHP2Bridge
