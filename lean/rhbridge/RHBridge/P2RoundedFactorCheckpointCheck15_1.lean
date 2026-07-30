import RHBridge.P2RoundedFactorCheckpointData15

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel15FactorChunk1 :
    P2RoundedFactorCheckpointData.panel15Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨15, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel15Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨15, by decide⟩ := by
  decide +kernel

theorem panel15Prefix4_eq :
    P2RoundedFactorCheckpointData.panel15Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk1.1

theorem panel15Prefix5_eq :
    P2RoundedFactorCheckpointData.panel15Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk1.2.1

theorem panel15Prefix6_eq :
    P2RoundedFactorCheckpointData.panel15Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk1.2.2.1

theorem panel15Prefix7_eq :
    P2RoundedFactorCheckpointData.panel15Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨15, by decide⟩ := by
  exact panel15FactorChunk1.2.2.2

end RHP2Bridge
