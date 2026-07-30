import RHBridge.P2RoundedFactorCheckpointData23

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel23FactorChunk1 :
    P2RoundedFactorCheckpointData.panel23Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨23, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel23Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨23, by decide⟩ := by
  decide +kernel

theorem panel23Prefix4_eq :
    P2RoundedFactorCheckpointData.panel23Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk1.1

theorem panel23Prefix5_eq :
    P2RoundedFactorCheckpointData.panel23Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk1.2.1

theorem panel23Prefix6_eq :
    P2RoundedFactorCheckpointData.panel23Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk1.2.2.1

theorem panel23Prefix7_eq :
    P2RoundedFactorCheckpointData.panel23Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨23, by decide⟩ := by
  exact panel23FactorChunk1.2.2.2

end RHP2Bridge
