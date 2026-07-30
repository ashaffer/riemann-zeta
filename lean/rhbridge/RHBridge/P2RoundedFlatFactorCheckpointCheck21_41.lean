import RHBridge.P2RoundedFlatFactorCheckpointData21

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel21FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel21FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel21FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel21TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel21FlatComponentChunk41

end RHP2Bridge
