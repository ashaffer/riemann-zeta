import RHBridge.P2RoundedFactorCheckpointData0

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel0FactorChunk4 :
    P2RoundedFactorCheckpointData.panel0Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨0, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel0Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨0, by decide⟩ := by
  decide +kernel

theorem panel0Prefix16_eq :
    P2RoundedFactorCheckpointData.panel0Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk4.1

theorem panel0Prefix17_eq :
    P2RoundedFactorCheckpointData.panel0Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk4.2.1

theorem panel0Prefix18_eq :
    P2RoundedFactorCheckpointData.panel0Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk4.2.2.1

theorem panel0Prefix19_eq :
    P2RoundedFactorCheckpointData.panel0Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨0, by decide⟩ := by
  exact panel0FactorChunk4.2.2.2

end RHP2Bridge
