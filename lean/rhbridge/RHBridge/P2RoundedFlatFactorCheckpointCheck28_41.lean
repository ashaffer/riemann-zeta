import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk41 :
    P2RoundedFactorCheckpointData.panel28FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd17_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd17 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨17, by decide⟩ := by
  exact panel28FlatComponentChunk41

end RHP2Bridge
