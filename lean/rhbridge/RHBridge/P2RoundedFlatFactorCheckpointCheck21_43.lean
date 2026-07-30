import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk43 :
    P2RoundedFactorCheckpointData.panel21FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨19, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd19_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd19 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨19, by decide⟩ := by
  exact panel21FlatComponentChunk43

end RHP2Bridge
