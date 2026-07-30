import RHBridge.P2RoundedFactorCheckpointData4

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel4FactorChunk4 :
    P2RoundedFactorCheckpointData.panel4Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨4, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel4Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨4, by decide⟩ := by
  decide +kernel

theorem panel4Prefix16_eq :
    P2RoundedFactorCheckpointData.panel4Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk4.1

theorem panel4Prefix17_eq :
    P2RoundedFactorCheckpointData.panel4Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk4.2.1

theorem panel4Prefix18_eq :
    P2RoundedFactorCheckpointData.panel4Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk4.2.2.1

theorem panel4Prefix19_eq :
    P2RoundedFactorCheckpointData.panel4Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨4, by decide⟩ := by
  exact panel4FactorChunk4.2.2.2

end RHP2Bridge
