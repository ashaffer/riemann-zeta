import RHBridge.P2RoundedFlatFactorCheckpointData28

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel28FlatComponentChunk33 :
    P2RoundedFactorCheckpointData.panel28FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel28FlatOdd9_eq :
    P2RoundedFactorCheckpointData.panel28FlatOdd9 =
      (P2RoundedFactorCheckpointData.panel28TruncatedOddComponents).get ⟨9, by decide⟩ := by
  exact panel28FlatComponentChunk33

end RHP2Bridge
