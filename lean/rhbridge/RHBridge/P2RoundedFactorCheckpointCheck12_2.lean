import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk2 :
    P2RoundedFactorCheckpointData.panel12Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix8_eq :
    P2RoundedFactorCheckpointData.panel12Prefix8 =
      normalizedPrefixTermAtomApprox ⟨8, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk2.1

theorem panel12Prefix9_eq :
    P2RoundedFactorCheckpointData.panel12Prefix9 =
      normalizedPrefixTermAtomApprox ⟨9, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk2.2.1

theorem panel12Prefix10_eq :
    P2RoundedFactorCheckpointData.panel12Prefix10 =
      normalizedPrefixTermAtomApprox ⟨10, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk2.2.2.1

theorem panel12Prefix11_eq :
    P2RoundedFactorCheckpointData.panel12Prefix11 =
      normalizedPrefixTermAtomApprox ⟨11, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk2.2.2.2

end RHP2Bridge
