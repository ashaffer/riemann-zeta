import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk45 :
    P2RoundedFactorCheckpointData.panel21FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd21_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd21 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨21, by decide⟩ := by
  exact panel21FlatComponentChunk45

end RHP2Bridge
