import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk15 :
    P2RoundedFactorCheckpointData.panel15Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix60_eq :
    P2RoundedFactorCheckpointData.panel15Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk15.1

theorem panel15Prefix61_eq :
    P2RoundedFactorCheckpointData.panel15Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk15.2.1

theorem panel15Prefix62_eq :
    P2RoundedFactorCheckpointData.panel15Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk15.2.2.1

theorem panel15Prefix63_eq :
    P2RoundedFactorCheckpointData.panel15Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk15.2.2.2

end RHP2Bridge
