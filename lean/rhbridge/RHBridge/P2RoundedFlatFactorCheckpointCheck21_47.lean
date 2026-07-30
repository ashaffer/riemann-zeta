import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk47 :
    P2RoundedFactorCheckpointData.panel21FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨23, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd23_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd23 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨23, by decide⟩ := by
  exact panel21FlatComponentChunk47

end RHP2Bridge
